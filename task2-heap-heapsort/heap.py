class MaxHeap:
    """Max-Heap Data Structure (ADT) implemented with a Python list."""
    
    def __init__(self):
        self.heap = []  # Array representation of the heap

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _heapify_up(self, index):
        """Restore max-heap property by bubbling up."""
        while index > 0:
            parent = self._parent(index)
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def _heapify_down(self, index):
        """Restore max-heap property by bubbling down."""
        n = len(self.heap)
        while True:
            largest = index
            left = self._left_child(index)
            right = self._right_child(index)

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def insert(self, key):
        """Insert a new element into the max-heap (O(log n))."""
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        """Remove and return the maximum element (O(log n))."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_val

    def peek(self):
        """Return the maximum element without removing it (O(1))."""
        return self.heap[0] if self.heap else None

    def build_heap(self, arr):
        """Build a max-heap from an unsorted array (O(n))."""
        self.heap = arr[:]
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)


def heap_sort(arr):
    """Heap Sort Algorithm (in-place, O(n log n)) using Max-Heap."""
    if not arr:
        return arr

    # Build max-heap
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)   # helper function below

    # Extract max repeatedly
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)

    return arr


def _heapify(arr, n, i):
    """Internal helper for heap_sort (max-heapify)."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)
