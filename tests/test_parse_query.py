# -*- coding: utf-8 -*-

import unittest
from ddt import ddt, data, unpack
from threading import Lock

from dns import DnsDatabase
from loaddnsdb import LoadMocksBasic
import searchdb
from parse_query import parse_query

# sample: DnsRecord(name='www.uwmedicine.org.', type='TXT', data='THE UW Medicine')


def has_match(search_str, dict):
    terms = search_str.split()
    # flattened strings
    strings = (s for l in dict.values() for s in l)
    # terms should match some of the strings
    result = any(t in s for t in terms for s in strings)
    return result


@ddt
class ParseQueryTest(unittest.TestCase):
    """test parse_query"""
    dns_db = None

    @classmethod
    def setUpClass(cls):
        load_mocks = LoadMocksBasic()
        cls.dns_db = DnsDatabase(load_mocks(), searchdb.search_db_all_text_lower)

    @classmethod
    def tearDownClass(cls):
        cls.dns_db = None

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
        # ("txt admin@uw.edu",),
        ("a txt cname txt.cname.a.uw.edu.",),
    )
    @unpack
    def test_parse_query(self, search_str):
        dict = parse_query(ParseQueryTest.dns_db, search_str)
        assert has_match(search_str, dict)
