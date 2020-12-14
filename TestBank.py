import unittest
import day14.moban
from ddt import ddt
from ddt import data
from ddt import unpack
from day16.utils.DataRead import DataRead

data1 = DataRead("database",database="bank",tablename="bankzhanghu",user="root",password="").list

@ddt
class TestBank(unittest.TestCase):
    @data(*data1)
    @unpack
    def testTakeMoney(self,a,b,c):
        d=0
        day14.moban.bank["张三"] = {"account": "admin", "password": "admin", "money": 2000}

        s = day14.moban.bank_takeMoney(a,b,c)
        self.assertEqual(s, d)



