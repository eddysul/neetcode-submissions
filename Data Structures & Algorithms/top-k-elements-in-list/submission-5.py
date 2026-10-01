class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # from collections import Counter
        c = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]

        for num, cnt in c.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        # for i in reversed(range(len(freq))):
        #     print(i)

        

                

