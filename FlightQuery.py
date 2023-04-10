#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 21:30:21 2023

@author: finnkruger
"""
from SortedTableMap import *

class FlightQuery(SortedTableMap):
    '''An application of SortedTableMap, used to query tickets of expected period'''
    
    class Key:
        __slots__ = "_origin", "_dest", "_date", "_time"
        def __init__(self, origin, dest, date, time):
            self._origin = origin
            self._dest = dest
            self._date = date
            self._time = time
        
        def __lt__(self, other):
            if self._origin < other._origin:
                return True
            elif self._origin == other._origin:
                if self._dest < other._dest:
                    return True
                elif self._dest == other._dest:
                    if self._date < other._date:
                        return True
                    elif self._date == other._date:
                        if self._time < other._time:
                            return True
            return False
        
        def __le__(self, other):
            return self < other or self == other

        def __eq__(self, other):
            return self._origin == other._origin and \
                   self._dest == other._dest and \
                   self._date == other._date and \
                   self._time == other._time

    def query(self, k1, k2):
        '''Returns a list of flights whose keys are lexicographically between k1 and k2'''
        return [(item._key._origin, item._key._dest, item._key._date, item._key._time, item._value) 
                for item in self._table if k1 <= item._key <= k2]
    
    
a = FlightQuery()
s = [("A", "B", 622, 1200, "No1"), ("A", "B", 622, 1230, "No2"), ("A", "B", 622, 1300, "No3")]
for each in s:
    key = a.Key(each[0], each[1], each[2], each[3])
    value = each[4]
    a[key] = value
print(len(a))

k1 = a.Key("A", "B", 622, 1200)
k2 = a.Key("A", "B", 622, 1300)
print(a.query(k1, k2))