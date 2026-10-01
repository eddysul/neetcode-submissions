class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[j] = target-nums[i]

        # Iterate once and for i store, key: target-nums[i], value: i
        # Iterate twice and for each j, if nums[j] exists as key value, 
        # If so, return j, value

    #    i       0,  1, 2, 3
    #    nums[i] [3, 4, 5, 6], target = 7

    #     {
    #         4: 0
    #         3: 1
    #         2: 2
    #         1: 3
    #     }

    #     {
    #         0: 3
    #         1: 4
    #         2: 5
    #         3: 6
    #     }


        difference = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in difference:
                return [difference[diff], i]
            difference[n] = i
        
            