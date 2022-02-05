from dataclasses import dataclass, asdict


@dataclass
class DnsRecord:
    '''holds a (simplified) DNS record info'''
    name: str
    type: str
    data: str

    def __lt__(self, other):
        # for sorted() to use
        return self.name < other.name

    def items(self):
        '''as dictionary items'''
        return asdict(self).items()
