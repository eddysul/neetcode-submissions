class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Non-optimal way: Sorting
            # Sort and then find sequence till it stops, record max (O n log n)
        # Kind of like bucket sort
            # create array with length max value + 1
            # example 1: [0]*21 so index 0 to 21
            # then, for each val, the index corresponds to it, so just make it equal to 1, like a tick
            # then, iterate through this list one more time and find max of consecutive 
            # then, it depends on max value so O(max_val)
        # Assumptions: Ask about negatives and check base, edge cases
        # Approach 2: Bucket Sort First
        # Bucket sort first to get O(n)
            # Use counter to get count first
            # Then, make array where count is index and bucket is number of values
        # Ex.: [[2,3]]


        # Approach 3: Use hashmap counters and only consider first element
        # Ex.: First create Count of each element O(n)
        # {2: 1, 20: 1, 4: 2, 10: 1, 3: 1, 5: 1}
        # Then iterate again through list, for each element, we lookup in counts for element + 1
        # So for 2, it would be 3, 4, 5, until we are done max O(n)
        # Idk if this is still O(n^2)
        # Edited approach, only do this for "start" of sequence, which means nums[i-1] doesn't exist, this elminiates trying for each number

        c = Counter(nums)
        set_nums = set(nums)
        max_length = 0

        for num in set_nums:
            if num-1 not in set_nums: # start of sequence O(1) as its set
                length = 1
                while num+length in set_nums:
                    length += 1
                max_length = max(length, max_length)
        return max_length
            

