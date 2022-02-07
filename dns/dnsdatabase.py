from typing import Iterable, Callable, Sequence
import logging

from dns.dnsrecord import DnsRecord
from searchdb import SearchScore


class DnsDatabase:
    '''a searchable database of DnsRecords'''

    def __init__(self, load_fn: Sequence[DnsRecord], search_score_fn: SearchScore):
        self.search_score_fn = search_score_fn
        self.records: Iterable = [d for d in load_fn]

    def search(self, *terms, max=10, reverse=True, **kwargs):
        '''search database using the search_score_fn'''
        searched = ((self.search_score_fn(r, *terms, **kwargs), r)
                    for r in self.records)
        matches = ((s, r) for s, r in searched if s)
        logging.debug(f"search: {matches}")
        return sorted(matches, reverse=reverse)[:max]
