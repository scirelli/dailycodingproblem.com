#!/usr/bin/env python3
import unittest

from tests.utils.test_decorators import it, describe

from main import findSmallestNumberOfBoats

fatPeopleWeightLists = [
    {'list': [100, 200, 150, 80], 'limit': 200, 'minNumberOfBoats': 3},
    {'list': [100, 100, 100, 100], 'limit': 200, 'minNumberOfBoats': 2},
    {'list': [1, 1, 1, 1], 'limit': 200, 'minNumberOfBoats': 1},
    {'list': [1], 'limit': 200, 'minNumberOfBoats': 1},
    {'list': [200], 'limit': 200, 'minNumberOfBoats': 1},
    {'list': [200, 200], 'limit': 200, 'minNumberOfBoats': 2},
    {'list': [200, 200, 200], 'limit': 200, 'minNumberOfBoats': 3},
    {'list': [200, 200, 200, 200], 'limit': 200, 'minNumberOfBoats': 4},
    {'list': [199, 200, 1, 1], 'limit': 200, 'minNumberOfBoats': 3},
    {'list': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'limit': 200, 'minNumberOfBoats': 1},
]


@describe
class TagValidator_is_Valid_TestCase(unittest.TestCase):
    """
    Run some tests
    """

    @it
    def test_0(self):
        """
        should return the minimum number of boats needed for save the fat people.
        """
        for test in fatPeopleWeightLists:
            result = findSmallestNumberOfBoats(test.get('list'), test.get('limit'))
            expected = test.get('minNumberOfBoats')
            print("[{}] \n\trequires {} boat(s)".format(', '.join([str(x) for x in test['list']]), result))
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
