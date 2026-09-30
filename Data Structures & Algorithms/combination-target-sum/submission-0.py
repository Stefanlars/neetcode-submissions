class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(curr, curr_sum, idx):

            if curr_sum == target:
                ans.append(curr[:])

            # base case to cut off the branch
            if curr_sum > target:
                return

            for i in range(idx, len(nums)):
                num = nums[i]

                curr.append(num)
                curr_sum += num

                backtrack(curr, curr_sum, i)

                curr.pop()
                curr_sum -= num

        backtrack([], 0, 0)
        return ans