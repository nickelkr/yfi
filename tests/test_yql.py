import unittest
from yfi.yql import Yql


class TestYQL(unittest.TestCase):

    def setUp(self):
        self.yql = Yql()

    def test_single_select(self):
        self.yql.select('*')
        self.assertEqual(self.yql.compiled(), 'select * from yahoo.finance.quotes')

    def test_single_where(self):
        self.yql.where('symbol')
        self.assertEqual(self.yql.compiled(), 'where symbol')

    def test_single__in(self):
        self.yql._in('TSLA')
        self.assertEqual(self.yql.compiled(), 'in ("TSLA")')

    def test_chaining(self):
        compiled = 'select * from yahoo.finance.quotes where symbol in ("TSLA")'
        self.yql.select('*').where('symbol')._in('TSLA')
        self.assertEqual(self.yql.compiled(), compiled)

    def test_sequence(self):
        compiled = 'select * from yahoo.finance.quotes where symbol in ("TSLA")'
        self.yql.select('*')
        self.yql.where('symbol')
        self.yql._in('TSLA')
        self.assertEqual(self.yql.compiled(), compiled)

    def yes(self):
        return True


if __name__ == '__main__':
    unittest.main()