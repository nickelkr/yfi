import unittest
from yfi.yql import Yql


class TestYQL(unittest.TestCase):

    def setUp(self):
        self.yql = Yql()

    def test_single_select(self):
        self.yql.select('*')
        self.assertEqual(self.yql.selects(), [('*',)])

    def test_single_where(self):
        self.yql.where('symbol')
        self.assertEqual(self.yql.wheres(), [('symbol',)])

    def test_single__in(self):
        self.yql._in('TSLA')
        self.assertEqual(self.yql._ins(), [('TSLA',)])

    def test_chaining(self):
        self.yql.select('*').where('symbol')._in('TSLA')
        self.assertEqual(self.yql.selects(), [('*',)])
        self.assertEqual(self.yql.wheres(), [('symbol',)])
        self.assertEqual(self.yql._ins(), [('TSLA',)])

if __name__ == '__main__':
    unittest.main()