class Solution:
    def trap(self, height: List[int]) -> int:
        
        # approach we get the tallest possible value and we use a seperate pointer to track 
        max_lefts = [0] * len(height)
        max_rights = [0] * len(height)
        curr_lmax = 0
        curr_rmax = 0

        l = 0
        r = len(height) - 1

        ans = 0

        while l < len(height) and r >= 0:
            max_lefts[l] = curr_lmax
            max_rights[r] = curr_rmax

            curr_lmax = max(curr_lmax, height[l])
            curr_rmax = max(curr_rmax, height[r])

            r -= 1
            l += 1
        
        for i in range(len(height)):

            calc = min(max_lefts[i], max_rights[i]) - height[i]

            if calc > 0:
                ans += calc

        return ans

