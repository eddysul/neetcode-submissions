class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hold dictionary where key is str and value is [] -> {'act': []}
            # Iterate through each value in strs
            # At each string, if sorted version of it exists in dict as key, add original to value list
            # If not, create new list and add it ther
        # return the lists

        from collections import defaultdict
        d = defaultdict(list)
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            d[sorted_word].append(word)
        
        res = []
        for val in d.values():
            res.append(val)
        return res