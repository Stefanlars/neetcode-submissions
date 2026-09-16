class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, bot = 0, len(matrix) - 1

        while top <= bot:

            if target > matrix[top][-1]:
                top += 1
            elif target < matrix[bot][0]:
                bot -= 1
            else:
                break
        if bot < top:
            return False

        l, r = 0, len(matrix[0])

        while l <= r:

            mid = (l + r) // 2

            if matrix[bot][mid] == target:
                return True
            if matrix[bot][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False