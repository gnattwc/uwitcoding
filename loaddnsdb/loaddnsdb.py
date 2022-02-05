from typing import Sequence

from dns import DnsRecord

class LoadDnsDbInterface:
    '''LoadMocks interface'''

    def __call__(self) -> Sequence[DnsRecord]:
        pass
