from dataclasses import dataclass

@dataclass
class DnsRecord:
    fqdn: str
    type: str
    data: str

    def __lt__(self, other):
        # for sorted() to use
        return self.fqdn < other.fqdn