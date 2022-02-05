from random import randint

from dns import DnsRecord

def search_db_basic(r: DnsRecord, *terms):
    counts = (str(r).count(t) for t in terms)
    return sum(counts)

def search_db_test(r: DnsRecord, *terms):
    return randint(1,20)