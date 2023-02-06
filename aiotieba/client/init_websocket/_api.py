import time
from typing import List

from .._core import TbCore
from .._helper import jsonlib
from ..exception import TiebaServerError
from ._classdef import WsMsgGroupInfo
from .protobuf import UpdateClientInfoReqIdl_pb2, UpdateClientInfoResIdl_pb2

CMD = 1001


def pack_proto(core: TbCore, secret_key: str) -> bytes:
    req_proto = UpdateClientInfoReqIdl_pb2.UpdateClientInfoReqIdl()
    req_proto.data.bduss = core._BDUSS
    device = {
        'subapp_type': 'mini',
        'cuid': core.cuid,
        '_os_version': '9',
        '_client_version': core.post_version,
        'net_type': '1',
        '_phone_screen': '720,1280',
        'pversion': '1.0.3',
        '_msg_status': '1',
        'cuid_gid': '',
        '_phone_imei': '000000000000000',
        'from': "1021099l",
        'cuid_galaxy2': core.cuid_galaxy2,
        'model': 'SM-G988N',
        '_pic_quality': '0',
        '_client_type': '2',
        #'channel_id': '4609820899808533744',
        'timestamp': str(int(time.time() * 1e3)),
    }
    req_proto.data.device = jsonlib.dumps(device, separators=(',', ':'))
    req_proto.data.secretKey = secret_key
    req_proto.data.width = 105
    req_proto.data.height = 105
    req_proto.data.stoken = core._STOKEN
    req_proto.cuid = f"{core.cuid}|com.baidu.tieba_mini{core.post_version}"

    return req_proto.SerializeToString()


def parse_body(body: bytes) -> List[WsMsgGroupInfo]:
    res_proto = UpdateClientInfoResIdl_pb2.UpdateClientInfoResIdl()
    res_proto.ParseFromString(body)

    if code := res_proto.error.errorno:
        raise TiebaServerError(code, res_proto.error.errmsg)

    groups = [WsMsgGroupInfo()._init(p) for p in res_proto.data.groupInfo]

    return groups
