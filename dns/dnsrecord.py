from dataclasses import dataclass, asdict


@dataclass(order=True, frozen=True)
class DnsRecord:
    '''holds a (simplified) DNS record info'''
    name: str
    type: str
    data: str

    def items(self):
        '''as dictionary items'''
        return asdict(self).items()
