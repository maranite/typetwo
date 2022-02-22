from datetime import date, datetime
import types
from typing import Any, AnyStr, Callable, Dict, List, Tuple, Union
from .dictcomparer import DictComparer

class RowKey():
    """Encapsulates the fields used as the primary key for a record"""

    def __init__(self, *keys):
        """Encapsulates the fields used as the primary key for a record.
        ``keys``:  One of more key names (strings)"""
        # even though we have the FunKey class, accomodate a function being passed here
        if len(keys) == 1 and isinstance(keys[0], types.FunctionType):    
            self.__call__ = keys[0]
            self.keys = []
        else: 
            self.keys = keys
    
    def __call__(self, row : dict):
        """
        Returns a tuple of values from ``row`` which correspond to the given keys
        """
        if isinstance(row, dict):
            return tuple([row.get(key, None) for key in self.keys])
        raise NotImplementedError()
        
    def group_rows(self, rows : List[dict]):
        """Returns a dict where ``rows`` are grouped by this key"""
        document = {}
        for row in rows:
            document.setdefault(self(row), []).append(row)            
        return document
    
    def __iter__(self):
        """Iterates the key names"""
        return iter(self.keys)



class FunKey(RowKey):
    """Special case RowKey wraps a function"""
    def __init__(self, func_to_wrap):
        """Encapsulates the fields used as the primary key for a record."""
        self.__call__ = func_to_wrap
    
    def __iter__(self):
        raise StopIteration()



class NoKey(RowKey):
    """Special case RowKey which groups all rows under a common key, namely 'ungrouped'"""
    def __init__(self):
        """Encapsulates the fields used as the primary key for a record."""
        self.keys = []

    def __call__(self, row : dict):
        """
        Returns a tuple of values from ``row`` which correspond to the given keys
        """
        if isinstance(row, dict):
            return "ungrouped"
