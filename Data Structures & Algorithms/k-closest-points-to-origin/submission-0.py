class Solution:
    import math
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Need a data structure to hold the distance and comapre if another one beats it
        # Ideally, a heap that stores k values (closest) and iterate once over all n points
        # Since its min values, we want to store in a max heap that always holds k largest values, so if anything smaller comes in we pop out.
        max_heap = []

        for i, coord in enumerate(points): # O(n)
            x, y = coord[0], coord[1]
            dist = math.sqrt(x**2 + y**2)
        
            heapq.heappush(max_heap, (-dist, coord)) # O(log k)
            if len(max_heap) > k:
                heapq.heappop(max_heap) # O(log k)
        
        res = []
        for point in max_heap:
            res.append(point[1])
        return res
            


            

        

