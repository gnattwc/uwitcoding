from dns.dnsdatabase import DnsRecord
from loadmocks.loadmocks import LoadMocksInterface

class LoadMocksBasic(LoadMocksInterface):
    def __call__(self):
        return (DnsRecord(*d) for d in SAMPLE_DNS )

SAMPLE_DNS = [
    ("english", "A", "192.168.1.45"),
    ("washington.edu.", "A", "128.95.155.134"),
    ("uw.edu.", "CNAME", "x3dard.uw.edu"),
    ("www.uwmedicine.org.", "TXT", "THE UW Medicine"),
    ("english.washington.edu.", "A", "192.168.1.45"),
    ("v23488023.s.uw.edu.", "TXT", "some text"),
]

