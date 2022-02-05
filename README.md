# uwitcoding
UW IT Coding Challenge

## setup
- install python 3.10 - e.g. https://www.anaconda.com/products/individual
- activate virtualenv - e.g. `conda activate base`
- ```pip install -r requirements.txt```  -- only needed for unit tests

## parse_query demo
```python parse_query.py```

## to run unit tests
```python -m unittest```

## note:
The instructions say the output looks like
```
{
    "name": ["itconnect.uw.edu.", "english"],
    "type": ["A"],
    "data": []
}
```
but I wasn't sure exactly what the format means.  The instructions also say the details are deliberately ambiguous.

So... for my parse_query,
1. the input string is interpreted as search terms separated by spaces
2. its output are the dns records that
   1. match the search terms
   2. sorted by number of search term matches, highest first
   3. "transposed" into the dict format, sorted by the most matched record starting from the left

```
{
    'name': ['www.uwmedicine.org.', 'v23488023.s.uw.edu.', 'english.washington.edu.', 'english'],
    'type': ['TXT', 'TXT', 'CNAME', 'A'],
    'data': ['THE UW Medicine', 'reserved by someone', '192.168.1.45', '192.168.1.45']
}
```