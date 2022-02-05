from dns.dnsrecord import DnsRecord
from loaddnsdb.loaddnsdb import LoadDnsDbInterface


class LoadFromFile(LoadDnsDbInterface):
    def __init__(self, filepath):
        self.filepath = filepath

    def __call__(self):
        pass
