class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        # approach go backwards in temperatures
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):

            how_far = 0

            while len(stack) and stack[-1][0] <= temperatures[i]:
                stack.pop()

            if len(stack):
                how_far = stack[-1][1] - i

            result[i] =  how_far

            stack.append((temperatures[i], i))

            

        return result