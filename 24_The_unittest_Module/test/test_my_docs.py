import doctest
import unittest
import my_docs


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(my_docs))
    return tests