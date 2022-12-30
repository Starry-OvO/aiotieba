import httpx

from .._exception import TiebaServerError
from .common.helper import jsonlib
from .common.typedef import Recovers


def pack_request(client: httpx.AsyncClient, fname: str, fid: int, name: str, pn: int) -> httpx.Request:
    request = httpx.Request(
        "GET",
        "https://tieba.baidu.com/mo/q/bawurecover",
        params={
            'fn': fname,
            'fid': fid,
            'word': name,
            'is_ajax': '1',
            'pn': pn,
        },
        headers=client.headers,
        cookies=client.cookies,
    )

    return request


def parse_response(response: httpx.Response) -> Recovers:
    response.raise_for_status()

    res_json = jsonlib.loads(response.content)
    if code := int(res_json['no']):
        raise TiebaServerError(code, res_json['error'])

    recovers = Recovers(res_json)

    return recovers