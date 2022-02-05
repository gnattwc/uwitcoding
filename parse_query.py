import logging
import sys

from dns import DnsDatabase
from loaddnsdb import LoadMocksBasic
import searchdb
from pprint import pprint


def parse_query(db: DnsDatabase, search_str: str) -> dict:
    '''find matches in DNS database'''
    logging.info(f"search_str='{search_str}'")
    terms = search_str.split()
    matches = db.search(*terms)
    logging.info(f"matches={matches}")
    # transpose matches for output requirement
    dict = {'name': [], 'type': [], 'data': []}  # type: ignore
    for (_, r) in matches:
        dict['name'].append(r.name)
        dict['type'].append(r.type)
        dict['data'].append(r.data)
    # logging.info(f"matches={dict}")
    return dict


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout,
                        encoding='utf-8', level=logging.INFO)
    load_mocks = LoadMocksBasic()

    db = DnsDatabase(load_mocks(), searchdb.search_db_all_text_lower)
    print('In Database:')
    [pprint(r) for r in db.records]  # type: ignore
    print()

    print('*** search str(DnsRecord) case insensitive')
    # sample: DnsRecord(name='www.uwmedicine.org.', type='TXT', data='THE UW Medicine')
    # this allows very specific search strings
    # output is sorted by number of string matches (str.count())
    pprint(parse_query(db, "name=\'www.uwmedicine.org.\'"), sort_dicts=False)
    print()
    pprint(parse_query(db, "txt"), sort_dicts=False)
    print()
    pprint(parse_query(db, "english 192.168"), sort_dicts=False)
    print()

    db.search_score_fn = searchdb.search_db_fields_only
    print('*** search only within the dns record fields')
    pprint(parse_query(db, "medicine"), sort_dicts=False)
    print()
    pprint(parse_query(db, "english some UW Medicine"), sort_dicts=False)
