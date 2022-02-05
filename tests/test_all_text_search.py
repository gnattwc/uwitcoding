# -*- coding: utf-8 -*-

import unittest
from ddt import ddt, data, unpack
from threading import Lock

from dns import DnsDatabase
from loaddnsdb import LoadMocksBasic
import searchdb
from parse_query import parse_query

# sample: DnsRecord(fqdn='www.uwmedicine.org.', type='TXT', data='THE UW Medicine')


def has_match_case_insensitive(search_str, matches):
    terms = search_str.split()
    # each matched record must contain at least one term - case insensitive
    result = all(any(t.lower() in str(r).lower() for t in terms) for s, r in matches)
    return result


def are_scores_descending(matches):
    scores = [s for s, r in matches]
    result = all(scores[i] >= scores[i + 1] for i in range(len(scores)-1))
    return result


@ddt
class AllTextSearchTest(unittest.TestCase):
    """test DnsDatabase.search()"""
    lock = Lock()
    dns_db = None

    @classmethod
    def get_db(cls):
        if AllTextSearchTest.dns_db is None:
            AllTextSearchTest.lock.acquire()
            load_mocks = LoadMocksBasic()
            cls.dns_db = DnsDatabase(load_mocks(), searchdb.search_db_all_text_lower)
            AllTextSearchTest.lock.release()
        return AllTextSearchTest.dns_db

    @data(
        ("washington",),
        ("english tea party",),
        ("UW",),
        ("english CNAME",),
        ("A 140.142",),
        ("washington.edu A",),
        ("uw.edu TXT",),
        ("itconnect.uw.edu.",),
        ("uwmedicine.org host.s.uw.edu CNAME",),
        ("128.208.5.219",),
        ("a",),
        ("uw edu english",),
        ("reserved",),
        ("txt admin@uw.edu",),
        ("a txt cname txt.cname.a.uw.edu.",),
    )
    @unpack
    def test_search_str_descending(self, search_str):
        terms = search_str.split()
        matches = AllTextSearchTest.get_db().search(*terms)
        assert has_match_case_insensitive(search_str, matches)
        assert are_scores_descending(matches)
