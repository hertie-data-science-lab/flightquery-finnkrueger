from SortedTableMap import *

class FlightQuery(SortedTableMap):
    '''An application of SortedTableMap, used to query tickets of expected period'''
    
    # define a Key class that will be used as the keys in the SortedTableMap
    class Key:
        # define the slots that the key will have
        __slots__ = "_origin", "_dest", "_date", "_time"
        
        # initialize the Key object 
        def __init__(self, origin, dest, date, time):
            self._origin = origin
            self._dest = dest
            self._date = date
            self._time = time
        
        # define the less-than operator for Key objects
        def __lt__(self, other):
            # compare the origin first
            if self._origin < other._origin:
                return True
            # if origins are equal, compare the destination
            elif self._origin == other._origin:
                if self._dest < other._dest:
                    return True
                # if destinations are equal, compare the date
                elif self._dest == other._dest:
                    if self._date < other._date:
                        return True
                    # if dates are equal, compare the time
                    elif self._date == other._date:
                        if self._time < other._time:
                            return True
            # if none of the above conditions are true, return False
            return False
        
        # define the less-than-or-equal-to operator for Key objects
        def __le__(self, other):
            # a Key object is less than or equal to another if it's less than it or equal to it
            return self < other or self == other

        # define the equality operator for Key objects
        def __eq__(self, other):
            # two Key objects are equal if all their attributes are equal
            return self._origin == other._origin and \
                   self._dest == other._dest and \
                   self._date == other._date and \
                   self._time == other._time

    # 
    def query(self, k1, k2):
        # iterate over the items in the SortedTableMap
        # and filter only the ones whose keys are between k1 and k2
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