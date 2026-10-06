class KthLargest:
    # Clarification Questions to ask
    # Are there always k integers in the stream or if there are less do we return different number?

    # Strategy should we use min or max heap? -> O(n) vs O(k) and we want O(k)
    # We want top k values, so if we create min heap
    # we will use minheap and 
    # Every add call, compare int to peek, so min value of heap which should be 3rd highest number
    # If int < min_val, don't add, else add int to heap and pop min_val
    # heapify and continue
    # then we should always have 3 largest vals and last val of minheap is always 3rd largest

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k or self.min_heap[0] < val:   
            heapq.heappush(self.min_heap, val)
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)

        return self.min_heap[0]
    
    # Time: Init -> O(n) where n is length of nums b/c it takes O(n) to heapify
    # add O(k) because each call only traverses max k elements
    # Total O(m * logk) for m calls of add()
        
