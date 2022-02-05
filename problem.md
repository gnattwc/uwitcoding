# DNS search

One of the systems our team maintains is a database of domain name system (DNS) records for the University of Washington. This database is used to generate the configuration files used by our DNS servers to respond to name lookups on campus and on the internet. We'll use a heavily simplified version of this database in the coding problem below.

Our (simplified) database table of DNS records has three columns:

- `name`, the fully-qualified domain name of the record
- `type`, the DNS record type, which is either `A`, `CNAME`, or `TXT`
- `data`, the record data associated with the `name` and `type`. The content of the `data` has a different meaning or format depending on the `type`:
    - `A` records have IP addresses in dotted-quad format as `data`, such as `128.95.155.134`
    - `CNAME` records have fully-qualified domain names as `data`, such as `alias.example.edu.`
    - `TXT` records can have data in any format, such as `reserved by foo@uw.edu` or `REQ8840000` or
      `MS=293192389` or `I like turtles`

For our purposes, a _fully-qualified domain name_ (FQDN) is a sequence of strings separated by and terminated with `.` ("dots"), where each component of the name ("subdomain") consists of alphanumeric characters. Example FQDNs in our database include:

- `washington.edu.`
- `uw.edu.`
- `www.uwmedicine.org.`
- `english.washington.edu.`
- `v23488023.s.uw.edu.`

We want to let users search our DNS data based on simple queries. Your task is to write a function `parse_query` in either Python or JavaScript which takes a single string as an argument and returns a dictionary. The dictionary returned should have `"name"`, `"type"`, and `"data"` as keys, and arrays of strings as values. The value of each key should be the strings extracted from the query that our application should match database records against to generate results for the user. So, this would be an example return value:

```json
    {
        "name": ["itconnect.uw.edu.", "english"],
        "type": ["A"],
        "data": []
    }
```

The details of doing this are up to you. There's deliberate ambiguity in this problem statement: we want you to use whatever approach you think makes sense to turn an unstructured query string into a structured set of search terms.

Here's some example queries to test your function against:

```
UW
english CNAME
A 140.142
washington.edu A
uw.edu TXT
itconnect.uw.edu.
uwmedicine.org host.s.uw.edu CNAME
128.208.5.219
a
uw edu english
reserved
txt admin@uw.edu
a txt cname txt.cname.a.uw.edu.
```