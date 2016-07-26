import unittest

from commonspy.db import SimpleMongoQueryBuilder


class SimpleMongoQueryBuilderTest(unittest.TestCase):
    def test_simple_equals_query(self):
        query = SimpleMongoQueryBuilder.start_new_query().equals('status', 'active').build()

        self.assertEquals({'status': 'active'}, query)
