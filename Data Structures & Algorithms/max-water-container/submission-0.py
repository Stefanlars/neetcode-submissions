class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        curr_max = 0

        while l < r:

            curr_max = max(curr_max, min(heights[l], heights[r]) * (r - l))

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return curr_max