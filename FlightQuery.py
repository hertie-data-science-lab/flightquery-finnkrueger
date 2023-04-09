from SortedTableMap import *


class FlightKey:
    def __init__(self, origin, dest, date, time):
        self.origin = origin
        self.dest = dest
        self.date = date
        self.time = time

    def __lt__(self, other):
        if self.date < other.date:
            return True
        elif self.date == other.date and self.time < other.time:
            return True
        elif self.date == other.date and self.time == other.time and self.origin < other.origin:
            return True
        elif self.date == other.date and self.time == other.time and self.origin == other.origin and self.dest < other.dest:
            return True
        else:
            return False

    def __le__(self, other):
        return self == other or self < other



class FlightQuery:
    def __init__(self):
        self._flight_data = SortedTableMap()

    def insert_flight(self, flight_key, flight_num):
        self._flight_data[flight_key] = flight_num

    def delete_flight(self, flight_key):
        del self._flight_data[flight_key]

    def find_range(self, start_key, end_key):
        for flight_key, flight_num in self._flight_data:
            if start_key <= flight_key <= end_key:
                yield flight_key, flight_num

    def query(self, origin, dest, date, start_time, end_time):
        start_key = FlightKey(origin, dest, date, start_time)
        end_key = FlightKey(dest, origin, date, end_time)
        results = []
        for flight_key, flight_num in self.find_range(start_key, end_key):
            if flight_key.origin == origin and flight_key.dest == dest and flight_key.date == date:
                results.append((flight_key.time, flight_num))
        return sorted(results)


a = FlightQuery()

a.insert_flight(FlightKey("A", "B", 622, 1200), "No1")
a.insert_flight(FlightKey("A", "B", 622, 1230), "No2")
a.insert_flight(FlightKey("A", "B", 622, 1300), "No3")

origin = "A"
dest = "B"
date = 622
time1 = 1200
time2 = 1300

results = a.query(origin, dest, date, time1, time2)
print(results)