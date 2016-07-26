import unittest

from commonspy.db import SimpleMongoQueryBuilder, Condition, MongoAnd


class SimpleMongoQueryBuilderTest(unittest.TestCase):
    def test_simple_equals_query(self):
        query = SimpleMongoQueryBuilder.start_new_query().equals('status', 'active').build()

        self.assertEquals({'status': 'active'}, query)


class MongoAndTest(unittest.TestCase):
    def test_simple_and_condition(self):
        condition = Condition.ne('status', 'active')
        query = MongoAnd.new_and_condition().add_condition(condition).build()

        self.assertEquals({'$and': [{'status': {'$ne': 'active'}}]}, query)

    def test_multiple_conditions(self):
        status_ne_active = Condition.ne('status', 'active')
        status_ne_inactive = Condition.ne('status', 'inactive')

        query = MongoAnd.new_and_condition().add_condition(status_ne_active).add_condition(status_ne_inactive).build()

        self.assertEquals({'$and': [{'status': {'$ne': 'active'}}, {'status': {'$ne': 'inactive'}}]}, query)
