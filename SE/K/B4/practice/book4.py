"""Independent teaching model — synthetic inputs and simplified assumptions."""
from math import exp, log

class BookingLedger:
    """Single-process model of a key-guarded reservation transaction."""

    def __init__(self, capacity):
        if capacity < 0:
            raise ValueError('capacity')
        self.capacity = capacity
        self.by_key = {}
        self.accepted = 0

    def book(self, key):
        if not key:
            raise ValueError('key')
        if key in self.by_key:
            return self.by_key[key]
        result = 'CONFIRMED' if self.accepted < self.capacity else 'REJECTED'
        self.by_key[key] = result
        if result == 'CONFIRMED':
            self.accepted += 1
        return result

    def cancel(self, key):
        if key not in self.by_key:
            return 'UNKNOWN'
        if self.by_key[key] == 'CANCELLED':
            return 'CANCELLED'
        if self.by_key[key] == 'REJECTED':
            return 'REJECTED'
        self.by_key[key] = 'CANCELLED'
        self.accepted -= 1
        return 'CANCELLED'

class VersionedTrip:

    def __init__(self):
        self.version = 0
        self.status = 'REQUESTED'

    def commit(self, expected_version, next_status):
        allowed = {'REQUESTED': {'HELD', 'CANCELLED'}, 'HELD': {'CONFIRMED', 'CANCELLED'}, 'CONFIRMED': {'BOARDED', 'CANCELLED'}, 'BOARDED': {'COMPLETED'}, 'COMPLETED': set(), 'CANCELLED': set()}
        if expected_version != self.version:
            return 'CONFLICT'
        if next_status not in allowed[self.status]:
            return 'INVALID_TRANSITION'
        self.status = next_status
        self.version += 1
        return 'OK'

if __name__ == '__main__':
    b=BookingLedger(1);  print([b.book('A'),b.book('A'),b.book('B')]);  t=VersionedTrip(); print(t.commit(0,'HELD'),t.commit(0,'CANCELLED'))
