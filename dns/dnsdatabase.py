from typing import Iterable, Callable
import logging


class DnsDatabase:
    '''a searchable database of DnsRecords'''

    def __init__(self, load_fn: Iterable, search_score_fn: Callable):
        self.search_score_fn = search_score_fn
        self.records: Iterable = [d for d in load_fn]

    def search(self, *terms, max=10, reverse=True, **kwargs):
        '''search database using the search_score_fn'''
        searched = ((self.search_score_fn(r, *terms, **kwargs), r)
                    for r in self.records)
        matches = ((s, r) for s, r in searched if s)
        logging.debug(f"search: {matches}")
        return sorted(matches, reverse=reverse)[:max]
