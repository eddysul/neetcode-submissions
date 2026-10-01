class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approaches
        # 1. Use hashmap to store Counts -> O(n) time, O(n) space
        # Then use max heap to store values
        # Get k values and return

        from collections import Counter
        import heapq

        count = Counter(nums)
        max_heap = []
        for num, freq in count.items():
            max_heap.append((-freq, num))

        heapq.heapify(max_heap)

        res = []
        while k > 0:
            res.append(heapq.heappop(max_heap)[1])
            k -= 1
        return res

        

                

