class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_map = [0] * 26

        char_map_check = [0] * 26

        for char in s1:
            char_map[ord(char.upper()) - ord('A')] += 1
            
        left = 0

        for right in range(len(s2)):
            char_map_check[ord(s2[right].upper()) - ord('A')] += 1

            while right - left + 1 > len(s1):

                char_map_check[ord(s2[left].upper()) - ord('A')] -= 1

                left += 1

            if char_map_check == char_map:
                return True

        return False