class Heap:
    def __init__(self, arr, size):
        self.heap = arr
        self.size = size
        return

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def parent(self, i):
        return (i-1)//2

    def sift_up(self, i):
        while i > 0 and self.parent(i) >= 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

# Need to verify that 1 2,3 4,5,6,7  8.9.10.11.12.13.14.15
    def sift_down(self, i):
        l = self.left(i)
        r = self.right(i)
        size = self.size
        largest = i

        if l < size and self.heap[largest] < self.heap[l]:
            largest = l
        if r < size and self.heap[largest] < self.heap[r]:
            largest = r

        if largest != i:
            self.swap(i, largest)
            self.sift_down(largest)
        return

    def swap(self, a, b):
        tmp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = tmp

    def heapify(self):
        i = self.size//2
        while i >= 0:
            self.sift_down(i)
            i = i - 1

    def extract_max(self):
        val = self.heap[0]
        self.swap(0, self.size - 1)
        self.size = self.size - 1
        self.sift_down(0)
        return val

    def get_sorted_array(self):
        arr = []
        while self.size > 0:
            arr.append(self.extract_max())
        return arr

    def insert(self, value):
        if self.size == len(self.heap):
            self.size += 1
            self.heap.append(value)
        else:
            self.heap[self.size-1] = value

        self.sift_up(self.size-1)


    def remove(self, index):
        self.heap[index]=float('inf')
        self.sift_up(index)
        print(self.heap)
        self.extract_max()

a = Heap([2,3,1,4,5,9,6], 7)
#a.sift_up(3)
print(a.heap)
a.heapify()
print(a.heap)
a.insert(10)
print(a.heap)
a.remove(2)
print(a.heap)
print(a.get_sorted_array())
print(a.heap)
