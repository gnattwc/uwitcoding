from typing import Iterable

from dns import DnsRecord


class LoadDnsDbInterface:
    '''LoadMocks interface'''

    def __call__(self) -> Iterable:
        pass
