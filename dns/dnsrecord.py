from dataclasses import dataclass, asdict


@dataclass
class DnsRecord:
    '''holds a (simplified) DNS record info'''
    fqdn: str
    type: str
    data: str

    def __lt__(self, other):
        # for sorted() to use
        return self.fqdn < other.fqdn

    def items(self):
        '''as dictionary items'''
        return asdict(self).items()
