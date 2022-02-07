from random import randint
from typing import Protocol

from dns.dnsrecord import DnsRecord

# sample: DnsRecord(name='www.uwmedicine.org.', type='TXT', data='THE UW Medicine')

# these functions are used to determine search score - higher the better

class SearchScore(Protocol):
    def __call__(self, r: DnsRecord, *terms, **kwargs):
        pass


def search_db_all_text(r: DnsRecord, *terms) -> int:
    '''str.count on DnsRecord's string

    >>> d = DnsRecord("mynameis", "TXT", "my name is")
    >>> search_db_all_text(d, 'name')  # returns 3 because DnsRecord has a 'name' field
    3
    '''
    counts = (str(r).count(t) for t in terms)
    return sum(counts)


def search_db_all_text_lower(r: DnsRecord, *terms) -> int:
    # str.count on DnsRecord's string
    counts = (str(r).lower().count(t.lower()) for t in terms)
    return sum(counts)


def search_db_fields_only(r: DnsRecord, *terms) -> int:
    '''
    str.count only in the DnsRecord fields case insensitive

    >>> d = DnsRecord("mynameis", "TXT", "my name is")
    >>> search_db_fields_only_lower(d, 'name')
    2
    '''
    counts = (v.count(t) for t in terms for v in r.astuple())
    return sum(counts)


def search_db_fields_only_lower(r: DnsRecord, *terms) -> int:
    '''
    str.count only in the DnsRecord fields case insensitive

    >>> d = DnsRecord("mynameis", "TXT", "my name is")
    >>> search_db_fields_only_lower(d, 'name')
    2
    '''
    counts = (v.lower().count(t.lower()) for t in terms for v in r.astuple())
    return sum(counts)


def search_db_all_text_by_type(r: DnsRecord, *terms, type='CNAME') -> int:
    # str.count on DnsRecord's string limited by type
    counts = (str(r).count(t) for t in terms if r.type.lower() == type.lower())
    return sum(counts)


def search_db_random(r: DnsRecord, *terms):
    return randint(1, 20)
