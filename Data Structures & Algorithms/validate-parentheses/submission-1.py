class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        stack = []
        for char in s:
            if char in paren_map:
                if len(stack) == 0:
                    return False
                
                if stack.pop() != paren_map[char]:
                    return False
            else:
                stack.append(char)

        if len(stack) > 0:
            return False
            
        return True