## COMP2090SEF / COMP8090SEF Course Project  
# Heap and Heap Sort
A study on Heap and Heap sort

**New Data Structure:** Max-Heap (complete binary tree stored in a Python list)
**New Algorithm:** Heap Sort (in-place O(n log n) sorting)

**Heap concept used**
- mh.peek() can quickly shows the biggest number
- mh.extract_max()takes out the biggest number and fixes the heap automatically
- mh.build_heap() will turns any messy list into a proper heap

**Heap sort concept used**
heap_sort(arr) calls the heap to build a Max-Heap from your unsorted array.
Then,itSwaps the biggest number with the last number in the array.
Next, it reduces the heap size by 1.
Finally, it fixes the heap again using heapify.


**How to Run**
```bash
cd task2-heap-heapsort
python test_heap.py
