class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(curr: List[int], i: int):
            nonlocal ans
            ans.append(curr[:])

            for i in range(i, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i + 1)
                curr.pop()
            
        backtrack([], 0)

        return ans
