from ast import Assert
from random import random
import unittest
from datetime import datetime, date, time
from src.typetwo import *

class TestIsoJson(unittest.TestCase):
    
    def test_loads(self):
        data = '{"datetime": "0001-01-01T00:00:00", "date": "0001-01-01", "time": "00:00:00"}'
        actual = IsoJson.loads(data)
        expected = {
            'datetime': datetime.min,
            'date' : date.min,
            'time' : time.min
        }
        self.assertEqual(expected, actual)

    def test_dumps(self):
        data = {
            'datetime': datetime.min,
            'date' : date.min,
            'time' : time.min
        }
        expected = '{"datetime": "0001-01-01T00:00:00", "date": "0001-01-01", "time": "00:00:00"}'
        actual = IsoJson.dumps(data)
        self.assertEqual(expected, actual)

    def test_dump_jsonl(self):
        data = [{'date' : date.min}, {'date' : date.min}, {'date' : date.min}]
        expected = '{"date": "0001-01-01"}\n{"date": "0001-01-01"}\n{"date": "0001-01-01"}'
        actual = IsoJson.dump_jsonl(data)
        self.assertEqual(expected, actual)