from typing import Iterable
from .dnsrecord import DnsRecord


class DnsDatabase:
    def __init__(self, load_fn: Iterable, search_score_fn):
        self.search_score_fn = search_score_fn
        self.records = [d for d in load_fn]

    def search(self, *terms, max=10):
        searched = ((self.search_score_fn(r, *terms), r) for r in self.records)
        matches = [(s,r) for s, r in searched if s]
        return sorted(matches)[:max]

    def search2(self, *terms, max=10, key=lambda t: t[0], reverse=False):
        searched = ((self.search_score_fn(r, *terms), r) for r in self.records)
        matches = [(s,r) for s, r in searched if s]
        return matches.sort(key=key, reverse=reverse)[:max]

