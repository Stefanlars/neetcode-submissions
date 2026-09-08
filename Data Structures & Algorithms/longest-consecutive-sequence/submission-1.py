class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        hm = {}
        currMax = 0
        for i in range(0, len(nums)):
            if nums[i] - 1 in hm:
                hm[nums[i]] = hm[nums[i] - 1] + 1
            else:
                hm[nums[i]] = 1

            currMax = max(currMax, hm[nums[i]])

        return currMax