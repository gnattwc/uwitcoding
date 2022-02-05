from dns.dnsrecord import DnsRecord
from loaddnsdb.loaddnsdb import LoadDnsDbInterface


class LoadMocksBasic(LoadDnsDbInterface):
    def __call__(self):
        return (DnsRecord(*d) for d in SAMPLE_DNS)


SAMPLE_DNS = [
    ("english", "A", "192.168.1.45"),
    ("washington.edu.", "A", "128.208.5.219"),
    ("uw.edu.", "CNAME", "x3dard.uw.edu"),
    ("www.uwmedicine.org.", "TXT", "THE UW Medicine"),
    ("www.english.washington.edu", "CNAME", "english.washington.edu."),
    ("v23488023.s.uw.edu.", "TXT", "reserved by someone"),
    ("uwitconnect", "CNAME", "itconnect.uw.edu."),
]
