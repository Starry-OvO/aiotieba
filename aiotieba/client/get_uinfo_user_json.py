import httpx

from .._exception import TiebaServerError
from .common.helper import jsonlib
from .common.typedef import UserInfo


def pack_request(client: httpx.AsyncClient, user_name: str) -> httpx.Request:
    request = httpx.Request(
        "GET",
        "http://tieba.baidu.com/i/sys/user_json",
        params={'un': user_name, 'ie': 'utf-8'},
        headers=client.headers,
        cookies=client.cookies,
    )

    return request


def parse_response(response: httpx.Response) -> UserInfo:
    response.raise_for_status()
    if not response.content:
        raise TiebaServerError(-1, "empty response")

    text = response.content.decode('utf-8', 'ignore')
    res_json = jsonlib.loads(text)

    user_dict = res_json['creator']

    user = UserInfo()
    user.user_id = user_dict['id']
    user.portrait = user_dict['portrait']

    return user