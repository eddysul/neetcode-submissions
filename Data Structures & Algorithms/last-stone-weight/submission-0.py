class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Start with heaviest 2 stones -> max heap? 
        # Clarification: Array is not sorted
        # [2, 3, 6, 2, 4]
        # [1]
        # Clarification: Are there always at least 2 stones in array? or one stone?

        # Base Case: Since its established theres always at least 1, if theres one return length of it.
        if len(stones) < 2:
            return stones[0]

        # Create maxHeap then pop both elements.
        # Its established that at max 1 will remain so we can get rid of both
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            # Since its max heap y (first element popped) is either greater or equal to x
            if y > x:
                heapq.heappush(max_heap, -(y-x))

        if len(max_heap) == 1:
            return -max_heap[0]
        else:
            return 0


        

