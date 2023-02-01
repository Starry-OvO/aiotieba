import binascii
import gzip
import hashlib
import json
import sys
import time

import aiohttp
import yarl
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from .._core import TbCore
from .._hash import _inv_rc4
from .._helper import jsonlib, log_exception, parse_json, send_request

SOFIRE_HOST = "sofire.baidu.com"


async def request(connector: aiohttp.TCPConnector, core: TbCore):

    app_key = '740017'  # 通过 p/5/aio 获取
    sec_key = '7aaf37cac7c3aaac3456b22832aabd56'
    xyus = hashlib.md5((core.android_id + core.uuid).encode('ascii')).hexdigest().upper() + '|0'
    xyus_md5 = hashlib.md5(xyus.encode('ascii')).hexdigest()
    curr_time = str(int(time.time()))

    params = {"module_section": [{'zid': xyus}]}

    req_body = jsonlib.dumps(params)
    req_body = gzip.compress(req_body.encode('utf-8'), compresslevel=-1, mtime=0)
    req_body_aes = core.aes_cbc_chiper.encrypt(pad(req_body, block_size=AES.block_size))
    req_body_md5 = hashlib.md5(req_body).digest()

    payload = aiohttp.payload.BytesPayload(
        req_body_aes + req_body_md5,
        content_type="application/x-www-form-urlencoded",
    )

    headers = {
        "x-device-id": xyus_md5,
        "x-plu-ver": 'x6/4.1.4.2',
    }

    path_combine = ''.join((app_key, curr_time, sec_key))
    path_combine_md5 = hashlib.md5(path_combine.encode('ascii')).hexdigest()
    temp2 = _inv_rc4(core.aes_cbc_sec_key, xyus_md5.encode('ascii'))
    req_query_skey = binascii.b2a_base64(temp2).decode('ascii')
    url = yarl.URL.build(
        scheme="https",
        host=SOFIRE_HOST,
        path=f"/c/11/z/100/{app_key}/{curr_time}/{path_combine_md5}",
        query_string=f'skey={req_query_skey}',
    )

    try:
        request = aiohttp.ClientRequest(
            aiohttp.hdrs.METH_POST,
            url,
            headers=headers,
            data=payload,
            loop=core._loop,
            proxy=core._proxy,
            proxy_auth=core._proxy_auth,
            ssl=False,
        )

        body = await send_request(request, connector, read_bufsize=1024)
        res_json = parse_json(body)

        res_query_skey = binascii.a2b_base64(res_json['skey'])
        res_aes_sec_key = _inv_rc4(res_query_skey, xyus_md5.encode('ascii'))
        aes_chiper = AES.new(res_aes_sec_key, AES.MODE_CBC, iv=b'\x00' * 16)
        res_data = binascii.a2b_base64(res_json['data'])
        res_data = unpad(aes_chiper.decrypt(res_data)[:-16], AES.block_size)  # [:-16] 用于移除尾部的16字节md5
        res_data = json.loads(res_data.decode('utf-8'))
        zid = res_data['token']

    except Exception as err:
        log_exception(sys._getframe(1), err)
        zid = ''

    return zid
