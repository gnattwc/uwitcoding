from dataclasses import astuple, dataclass, asdict, fields


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

    def __str__(self):
        cls = self.__class__
        # cls_name = cls.__name__
        res = []
        for f in fields(cls):
            value = getattr(self, f.name)
            # res.append(f'{f.name}={value}')
            res.append(f'{value}')
        return ' '.join(res)