from loadmocks.loadmocks import LoadMocksInterface
from dns.dnsdatabase import DnsRecord
from random import choice, randint

class LoadMocksRandom(LoadMocksInterface):
    def __init__(self, size=100):
        self.size = 100

    def __call__(self):
        return ()

    def mock_dns_record():
        pass
        # type = choice(SAMPLE_TYPE)
        # match type:
        #     case "CNAME":

        #     fqdn = choice(SAMPLE_FQDN)


SAMPLE_FQDN = [
    "washington.edu.",
    "uw.edu.",
    "www.uwmedicine.org.",
    "english.washington.edu.",
    "v23488023.s.uw.edu.",
]

SAMPLE_TYPE = [
    "A",
    "CNAME",
    "TXT",
]

def gen_ip():
    ip = ".".join(map(str, (randint(0, 255) for _ in range(4))))
    return ip