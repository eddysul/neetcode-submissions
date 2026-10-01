class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 1, 1, 1]
        #  Create prefix array, and suffix array of [1,1,1,1]
        #  then for each start at one position before and iterate and multiply values up till i-1
        # Multiply prefix and suffix array

        prefix, suffix = [1]*len(nums), [1]*len(nums)
        forward, backward = 1, 1
        
        for i in range(len(nums)):
            prefix[i] = forward
            forward *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = backward
            backward *= nums[i]

        res = []
        for i in range(len(nums)):
            res.append(prefix[i]*suffix[i])

        return res

        
