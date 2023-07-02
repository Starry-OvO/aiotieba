import bs4
import yarl

from ...const import WEB_BASE_HOST
from ...core import HttpCore
from ._classdef import BawuBlacklists


def parse_body(body: bytes) -> BawuBlacklists:
    soup = bs4.BeautifulSoup(body, 'lxml')
    bawu_blacklists = BawuBlacklists(soup)

    return bawu_blacklists


async def request(http_core: HttpCore, fname: str, pn: int) -> BawuBlacklists:
    params = [
        ('word', fname),
        ('pn', pn),
    ]

    request = http_core.pack_web_get_request(
        yarl.URL.build(scheme="https", host=WEB_BASE_HOST, path="/bawu2/platform/listBlackUser"), params
    )

    __log__ = "fname={fname}"  # noqa: F841

    body = await http_core.net_core.send_request(request, read_bufsize=64 * 1024)
    return parse_body(body)