from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.m= dict()
        self.deq = deque()

    def get(self, key: int) -> int:
        if key in self.m:
             value = self.m[key]
             self.deq.remove(key)
             self.deq.append(key)
             return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.m:
            if self.c >= 1:
                self.m[key] = value
                self.deq.append(key)
                self.c = self.c-1
            else:
                keyToRemove = self.deq[0]
                self.m.pop(keyToRemove)
                self.deq.popleft()
                self.deq.append(key)
                self.m[key] = value
        else:
            self.m[key] = value
            self.deq.remove(key)
            self.deq.append(key)
