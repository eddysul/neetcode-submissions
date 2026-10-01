class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Represent every string by frequency of characters
        # Assumptions: Is each string always lowercase, alphabet?
        # count array = [0]*26
        # c increment count
        # convert count array to tuple and use as key
        from collections import defaultdict
        
        res = defaultdict(list)

        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(word) 
        
        return list(res.values())
            