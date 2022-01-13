from ast import Assert
from random import random
import unittest
from src.typetwo import *

class TestTypeTwo(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.rows   = [{'a':1, 'b':x, 'c': random() } for x in range(10)]
        self.change = [{'a':1, 'b':x, 'c': random()} for x in range(10)]

    def test_rowkey_grouping_1(self):
        key = RowKey('a')
        grouped = key.group_rows(self.rows)        
        expected = 1
        actual = len(grouped.keys())
        self.assertEqual(expected, actual, "RowKeys not grouping correctly on 1 key")

    def test_rowkey_grouping_2(self):
        key = RowKey('a', 'b')
        grouped = key.group_rows(self.rows)        
        expected = len(self.rows)
        actual = len(grouped.keys())
        self.assertEqual(expected, actual, "RowKeys not grouping correctly on 2 keys")
        
    def test_rowkey_extraction(self):
        key = RowKey('a', 'b')
        row = self.rows[0]
        expected = (row['a'], row['b'])
        actual =  key(row)
        self.assertEqual(expected, actual, "RowKeys not extracting correctly")

    def test_type_two_1(self):
        key = RowKey('a', 'b')
        type_ii = TypeTwo(key, self.rows)
        self.assertFalse(type_ii.has_changes)
        expected = len(self.rows)
        items = [x for x in type_ii]
        actual = len(items)
        self.assertEqual(expected, actual, "TypeTwo not loading exiting rows")

    def test_type_two_process_row(self):
        key = RowKey('a', 'b')
        type_ii = TypeTwo(key, self.rows)
        row = self.change[0]
        type_ii.process_row(row)
        self.assertTrue(type_ii.has_changes, "TypeTwo process_row has_changes not working")
        changes = [q for q in type_ii if key(q) == key(row)]
        actual = len(changes)
        expected = 2
        self.assertEqual(expected, actual, "TypeTwo process_row not working")      

    def test_type_two_2(self):
        key = RowKey('a', 'b')
        type_ii = TypeTwo(key, self.rows)
        type_ii.process_rows(self.change)
        self.assertTrue(type_ii.has_changes, "has_changes not working")
        expected = len(self.rows) * 2
        items = [x for x in type_ii]
        actual = len(items) 
        self.assertEqual(expected, actual, "TypeTwo not processing change rows")

    def test_type_two_3(self):
        key = RowKey('a', 'b')
        type_ii = TypeTwo(key, self.rows)
        type_ii += self.change
        expected = len(self.rows) * 2
        items = [x for x in type_ii]
        actual = len(items) 
        self.assertEqual(expected, actual, "TypeTwo += not processing change rows")        