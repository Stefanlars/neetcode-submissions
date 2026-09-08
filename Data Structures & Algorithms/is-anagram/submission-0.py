from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = Counter(s)
        
        for char in t:
            sCount[char] -= 1

            if sCount[char] < 0:
                return False
        

        return sCount.total() == 0