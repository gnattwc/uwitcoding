import unittest
import doctest

from searchdb import searchdb
modules = [searchdb]

suite = unittest.TestSuite()
for mod in modules:
    suite.addTest(doctest.DocTestSuite(mod))
runner = unittest.TextTestRunner()
runner.run(suite)