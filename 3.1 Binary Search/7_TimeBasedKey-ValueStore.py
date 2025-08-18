# Time Based Key-Value Store

# Implement a time-based key-value data structure that supports:

#     Storing multiple values for the same key at specified time stamps
#     Retrieving the key's value at a specified timestamp

# Implement the TimeMap class:

#     TimeMap() Initializes the object.
#     void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
#     String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".

# Note: For all calls to set, the timestamps are in strictly increasing order.

# Example 1:

# Input:
# ["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]

# Output:
# [null, null, "happy", "happy", null, "sad"]

# Explanation:
# TimeMap timeMap = new TimeMap();
# timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
# timeMap.get("alice", 1);           // return "happy"
# timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
# timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
# timeMap.get("alice", 3);           // return "sad"

# Constraints:

#     1 <= key.length, value.length <= 100
#     key and value only include lowercase English letters and digits.
#     1 <= timestamp <= 1000

class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.hash_map:
            self.hash_map[key] = []
        self.hash_map[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if not self.hash_map.get(key):
            return ""
        l, r = 0, len(self.hash_map[key]) - 1
        recent = ""
        while l <= r:
            m = l + (r - l) // 2
            mid_ts, val = self.hash_map[key][m]
            if mid_ts == timestamp:
                return val
            if mid_ts > timestamp:
                r = m - 1
            else:
                recent = val
                l = m + 1
        return recent


class TimeMap:

    def __init__(self):
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = []
        self.key_store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        values = self.key_store.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            ts, val = values[m]
            if ts <= timestamp:
                ans = val
                l = m + 1
            else:
                r = m - 1
        return ans
