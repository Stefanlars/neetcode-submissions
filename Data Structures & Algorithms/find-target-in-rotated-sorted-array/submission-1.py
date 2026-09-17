class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        pivotPoint = 0

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = l + (r-l) // 2

            if nums[r] > nums[mid]:
                r = mid
            else:
                l = mid + 1

        pivotPoint = r
        
        if target == nums[pivotPoint]:
            return pivotPoint
        
        if pivotPoint == 0:
            l = 0
            r = len(nums) - 1
        elif nums[len(nums) - 1] >= target > nums[pivotPoint]:
            l = pivotPoint
            r = len(nums) - 1
        else:
            l = 0
            r = pivotPoint

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        return -1