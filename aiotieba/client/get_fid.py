import httpx

from .._exception import TiebaServerError
from .common.helper import jsonlib


def pack_request(client: httpx.AsyncClient, fname: str) -> httpx.Request:
    request = httpx.Request(
        "GET",
        "http://tieba.baidu.com/f/commit/share/fnameShareApi",
        params={'fname': fname, 'ie': 'utf-8'},
        headers=client.headers,
        cookies=client.cookies,
    )

    return request


def parse_response(response: httpx.Response) -> int:
    response.raise_for_status()

    res_json = jsonlib.loads(response.content)
    if code := int(res_json['no']):
        raise TiebaServerError(code, res_json['error'])

    if not (fid := int(res_json['data']['fid'])):
        raise TiebaServerError(-1, "fid is 0")

    return fid