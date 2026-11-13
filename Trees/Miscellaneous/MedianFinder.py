# Median from a data stream  (LC 295, Hard) — TWO HEAPS
# Problem: Implement a class to add integers from a data stream and return the median of all elements so far.
# Idea: max-heap `lo` holds the smaller half, min-heap `hi` the larger half;
# keep sizes equal (or lo one bigger). Median = top(s). add O(log n), median O(1).


import heapq
import random
import statistics

class MedianFinder:
    def __init__(self):
        self.lo = []      # max-heap via negatives
        self.hi = []      # min-heap

    def add_num(self, x):
        heapq.heappush(self.lo, -x)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))   # move the largest of lo to hi
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def find_median(self):
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2

if __name__ == "__main__":
    m = MedianFinder()
    out = []
    for x in [5, 15, 1, 3]:
        m.add_num(x)
        out.append(m.find_median())
    assert out == [5.0, 10.0, 5.0, 4.0]

    random.seed(3)
    for _ in range(300):
        arr = [random.randint(-50, 50) for _ in range(random.randint(1, 40))]
        mf = MedianFinder()
        for i, x in enumerate(arr):
            mf.add_num(x)
            assert mf.find_median() == statistics.median(arr[:i + 1])
    print("Median Finder tests passed!!")
