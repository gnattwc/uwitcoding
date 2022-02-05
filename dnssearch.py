import argparse
import logging
import sys
import os
from pprint import pprint

from dns import DnsDatabase
from loadmocks import LoadMocksBasic
import searchdb

def main() -> int:
    ''' main() returns exit code '''
    # parser = argparse.ArgumentParser()
    # parser.add_argument('pathToConfig', help='path to deploy config file')
    # parser.add_argument('command', help='what to do',
    #                     choices=['get', 'create', 'update'])
    # parser.add_argument(
    #     '-m', '--max', help='max to list or unprovision', default=10)
    # args = parser.parse_args()

    # logging.basicConfig(stream=sys.stdout, encoding='utf-8', level=logging.INFO)
    # logger = logging.getLogger(os.path.basename(__file__))
    load_mocks = LoadMocksBasic()
    db = DnsDatabase( load_mocks(), searchdb.search_db_basic)
    print('In Database:')
    [pprint(r) for r in db.records]

    terms = ["english", "uw"]
    matches = db.search(*terms)
    print(f'Searching: {terms}:')
    [pprint(r) for r in matches]


if __name__ == '__main__':
    sys.exit(main())