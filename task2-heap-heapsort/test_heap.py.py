from heap import MaxHeap, heap_sort

print("1. Max-Heap Data Structure")
mh = MaxHeap()
numbers = [12, 11, 13, 5, 6, 7]
for num in numbers:
    mh.insert(num)

print("Inserted elements:", numbers)
print("Max element (peek):", mh.peek())
print("Extract max:", mh.extract_max())
print("Heap after extraction:", mh.heap, "\n")

print("2. Heap Sort Algorithm")
arr = [12, 11, 13, 5, 6, 7]
print("Original array :", arr)
sorted_arr = heap_sort(arr)
print("Sorted array   :", sorted_arr)
