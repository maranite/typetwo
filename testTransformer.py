import unittest
from datetime import datetime, date, time
from pytz import timezone, utc
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

    def test_dates_inplace(self):
        auto_parse = Transformer().enable_iso_dates()
        data = {'a' : {'dt': "2015-05-14"}}
        auto_parse(data)
        self.assertEqual(date(2015, 5, 14), data['a']['dt'])
        
    def test_dates_no_inplace(self):
        auto_parse = Transformer().enable_iso_dates()
        data = {'a' : {'dt': "2015-05-14"}}
        data2 = auto_parse(data, in_place=False)
        self.assertEqual(date(2015, 5, 14), data2['a']['dt'])
        self.assertEqual("2015-05-14", data['a']['dt'])

    def test_enable_datetimes_tz(self):        
        auto_parse = Transformer().enable_datetimes_tz(timezone("Etc/GMT+10"))
        expected = datetime(2015, 5, 14, 12, 0, 0, tzinfo=utc)        
        actual = auto_parse("2015-05-14T02:00:00")
        self.assertEqual(expected, actual)

    def test_enable_datetimes_tz_daylight_saving(self):        
        auto_parse = Transformer().enable_datetimes_tz(timezone("Australia/Brisbane"))
        actual = auto_parse("2022-05-14T11:00:00")
        expected = datetime(2022, 5, 14, 1, 0, 0, tzinfo=utc)        
        self.assertEqual(expected, actual)
