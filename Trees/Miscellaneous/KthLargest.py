# Kth largest element  (LC 215)  — HEAP
# Problem: Given an integer array nums and an integer k, return the kth largest element in the array.
# Idea: keep a MIN-heap of size k; its root is always the kth largest so far.
# O(n log k) time, O(k) space


import heapq
import random

def kth_largest(nums, k):
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

if __name__ == "__main__":
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

    random.seed(3)
    for _ in range(300):
        arr = [random.randint(-50, 50) for _ in range(random.randint(1, 40))]
        k = random.randint(1, len(arr))
        assert kth_largest(arr, k) == sorted(arr, reverse=True)[k - 1]
    print("Kth Largest tests passed!!")