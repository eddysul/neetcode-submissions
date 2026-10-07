class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # minHeap of size k, and only keep if greater than min value
        # Brute force would be sorting O(n log n)
        # Heap would be O(n log k)

        min_heap = []
        for num in nums: # O(n)
            heapq.heappush(min_heap, num) # O(log k)

            if len(min_heap) > k:
                heapq.heappop(min_heap) # O(log k)

        return min_heap[0]