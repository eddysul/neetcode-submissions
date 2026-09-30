class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # need 2 pointers, one that iterates through s, one that iterates through t
        # use 2 counters (hashmaps)

        from collections import defaultdict
        s_count = Counter(s)
        t_count = Counter(t)

        if s_count != t_count:
            return False
        return True