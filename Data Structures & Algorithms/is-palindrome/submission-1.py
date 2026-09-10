class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            

            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    return False
                
                l += 1
                r -= 1
                continue

            if not s[l].isalpha():
                l += 1
                
            if not s[r].isalpha():
                r -= 1
        return True