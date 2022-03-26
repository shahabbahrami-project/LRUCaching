import unittest
from main import LRUCache

class TestLRU(unittest.TestCase):

    def test_random_put_get(self):
        LRU = LRUCache(4)
        LRU.put(1,1)
        self.assertEqual(LRU.get(1), 1)
        LRU.put(2,2)
        self.assertEqual(LRU.get(2), 2)
        LRU.put(4,4)
        self.assertEqual(LRU.get(4), 4)
        self.assertEqual(LRU.get(3), -1)
        LRU.put(4,100)
        self.assertEqual(LRU.get(4), 100)
        LRU.put(5,5)
        LRU.put(6,6)
        self.assertEqual(LRU.get(1), -1)
        self.assertEqual(LRU.get(5), 5)



if __name__ == '__main__':
    unittest.main()
