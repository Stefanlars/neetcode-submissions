class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()

        def backtrack(curr=[], idx = 0):
            nonlocal ans

            ans.append(curr)

            if len(curr) == len(nums):
                return

            
            while idx < len(nums):

                curr.append(nums[idx])
                backtrack(curr[::], idx + 1)
                curr.pop()

                idx += 1
                while idx < len(nums) and nums[idx] == nums[idx - 1]:
                    idx += 1

        backtrack()

        return ans