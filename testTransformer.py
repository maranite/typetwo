import unittest
from datetime import datetime, date, time
from src.typetwo import *

class TestTransformer(unittest.TestCase):
    
    def test_dates_d_mm_y(self):
        auto_parse = Transformer().enable_dates('%d/%m/%Y', '%d-%b-%Y', '%d-%m-%Y')
        self.assertEqual(date(2015, 5, 14), auto_parse("14-MAY-2015"))
        self.assertEqual(date(2015, 5, 14), auto_parse("14-05-2015"))
        self.assertEqual(date(2015, 5, 14), auto_parse("14/05/2015"))

    def test_dates_iso(self):
        auto_parse = Transformer().enable_iso_dates()
        self.assertEqual(date(2015, 5, 14), auto_parse("2015-05-14"))
        self.assertEqual(time(12, 0, 0), auto_parse("12:00:00"))
        self.assertEqual(datetime(2015, 5, 14, 12, 0, 0), auto_parse("2015-05-14T12:00:00"))

