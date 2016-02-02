import unittest
from yfi.yql import Yql


class TestYQL(unittest.TestCase):

    def setUp(self):
        self.yql = Yql()


    def test_single_select(self):
        self.yql.select('*')
        self.assertIn('select * from yahoo.finance.quotes', self.yql.parts())

    def test_multi_select(self):
        self.yql.select('Ask', 'Bid')
        self.assertIn('select Ask, Bid from yahoo.finance.quotes', self.yql.parts())

    def test_select_all(self):
        self.yql.select()
        self.assertIn('select * from yahoo.finance.quotes', self.yql.parts())

    def test_single_where(self):
        self.yql.where('symbol')
        self.assertIn('where symbol', self.yql.parts())

    def test_single__in(self):
        self.yql._in('TSLA')
        self.assertIn('in ("TSLA")', self.yql.parts())

    def test_multi_in(self):
        self.yql._in('TSLA', 'GOOG')
        self.assertIn('in ("TSLA", "GOOG")', self.yql.parts())

    def test_and(self):
        self.yql._and()
        self.assertIn('and', self.yql.parts())

    def test_chaining(self):
        self.yql.select('*').where('symbol')._in('TSLA')
        self.assertIn('select * from yahoo.finance.quotes', self.yql.parts())
        self.assertIn('where symbol', self.yql.parts())
        self.assertIn('in ("TSLA")', self.yql.parts())

    def test_sequence(self):
        self.yql.select('*')
        self.yql.where('symbol')
        self.yql._in('TSLA')
        self.assertIn('select * from yahoo.finance.quotes', self.yql.parts())
        self.assertIn('where symbol', self.yql.parts())
        self.assertIn('in ("TSLA")', self.yql.parts())

    def test_symbol(self):
        self.yql.symbol('TSLA')
        self.assertIn('select * from yahoo.finance.quotes', self.yql.parts())
        self.assertIn('where symbol', self.yql.parts())
        self.assertIn('in ("TSLA")', self.yql.parts())




if __name__ == '__main__':
    unittest.main()