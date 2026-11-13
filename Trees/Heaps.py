class MaxHeap:                       # exactly the PDF class (0-indexed array)
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)                  # add at the end
        i = len(self.heap) - 1
        while i > 0:                             # heapify up
            parent = (i - 1) // 2
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def delete_root(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        last = self.heap.pop()
        self.heap[0] = last
        i = 0
        while True:                              # heapify down
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right
            
            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            
            else:
                break
        return root


def heap_insert_1idx(HEAP, N, VAL):

    N = N + 1
    POS = N
    if len(HEAP) <= N:
        HEAP.append(None)
    HEAP[N] = VAL
    while POS > 1:
        PAR = POS // 2
        if HEAP[POS] <= HEAP[PAR]:
            break
        HEAP[POS], HEAP[PAR] = HEAP[PAR], HEAP[POS]
        POS = PAR
    return N


def heap_delete_1idx(HEAP, N):

    ROOT = HEAP[1]
    LAST = HEAP[N]
    N = N - 1
    PTR, LEFT, RIGHT = 1, 2, 3
    HEAP[PTR] = LAST
    while LEFT <= N:
        if HEAP[PTR] >= HEAP[LEFT] and (RIGHT > N or HEAP[PTR] >= HEAP[RIGHT]):
            break
        if RIGHT > N or HEAP[RIGHT] <= HEAP[LEFT]:
            HEAP[PTR], HEAP[LEFT] = HEAP[LEFT], HEAP[PTR]
            PTR = LEFT
        else:
            HEAP[PTR], HEAP[RIGHT] = HEAP[RIGHT], HEAP[PTR]
            PTR = RIGHT
        LEFT = 2 * PTR
        RIGHT = LEFT + 1
    return ROOT, N


class MinHeap:                       # mirror of MaxHeap (min-heap figure in the PDF)
    def __init__(self):
        self.heap = []

    def insert(self, v):
        self.heap.append(v)
        i = len(self.heap) - 1
        while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
            p = (i - 1) // 2
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p

    def delete_root(self):
        if not self.heap:
            return None
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            i = 0
            n = len(self.heap)
            while True:
                l, r, s = 2 * i + 1, 2 * i + 2, i
                if l < n and self.heap[l] < self.heap[s]:
                    s = l
                if r < n and self.heap[r] < self.heap[s]:
                    s = r
                if s == i:
                    break
                self.heap[i], self.heap[s] = self.heap[s], self.heap[i]
                i = s
        return root


def heapify(arr, n, i):              # sink arr[i] within first n elements (max-heap)
    largest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):

    arr = list(arr)
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(arr, end, 0)

    return arr


def Heaps():
    h = MaxHeap()
    values = [40, 10, 30, 50, 60, 15]

    for v in values:
        h.insert(v)

    print("Heap:", h.heap, "  (expected [60, 50, 30, 10, 40, 15])")
    print("Deleted Root:", h.delete_root(), "  (expected 60)")
    print("After Deletion:", h.heap, "  (expected [50, 40, 30, 10, 15])")

    # PDF figure: insert 45,36,54,27,63,72,61,18 step by step (1-indexed pseudocode)
    print("\nPDF insertion figure — build max-heap from 45 36 54 27 63 72 61 18 (1-indexed algorithm)")

    HEAP, N = [None], 0

    for v in [45, 36, 54, 27, 63, 72, 61, 18]:
        N = heap_insert_1idx(HEAP, N, v)
        print(f"  insert {v:2d} -> {HEAP[1:N+1]}")

    print("  Final array (expected [72, 54, 63, 27, 36, 45, 61, 18]):", HEAP[1:N + 1])

    print("Deleting root with the 1-indexed algorithm:")

    root, N = heap_delete_1idx(HEAP, N)

    print(f"  deleted {root}; heap now {HEAP[1:N+1]}")

    # Min heap
    mh = MinHeap()

    for v in [40, 10, 30, 50, 60, 15]:
        mh.insert(v)

    print("\nMinHeap:", mh.heap)
    d = mh.delete_root()

    print("  delete_root ->", d, " now", mh.heap)

    # Index rules
    arr = [72, 54, 63, 27, 36, 45, 61, 18]

    print("\nIndex rules (0-indexed): parent(i)=(i-1)//2, left=2i+1, right=2i+2")

    for i in range(len(arr)):
        l, r = 2 * i + 1, 2 * i + 2
        print(f"  arr[{i}]={arr[i]:2d} parent={arr[(i-1)//2] if i else '-':>2} "
              f"left={arr[l] if l < len(arr) else '-':>2} right={arr[r] if r < len(arr) else '-':>2}")

    # Heap sort
    data = [40, 10, 30, 50, 60, 15, 5, 99, 1]

    print("\nHeap Sort:", data, "->", heap_sort(data))

if __name__ == "__main__":
    Heaps()