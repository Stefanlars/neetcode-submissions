from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm = defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))

            hm[key].append(st)


        return list(hm.values())