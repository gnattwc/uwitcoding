from dataclasses import astuple, dataclass, asdict


@dataclass(order=True, frozen=True)
class DnsRecord:
    '''holds a (simplified) DNS record info'''
    name: str
    type: str
    data: str

    def asdict(self):
        '''as dictionary'''
        return asdict(self)

    def astuple(self):
        '''return values as tuple'''
        return astuple(self)
