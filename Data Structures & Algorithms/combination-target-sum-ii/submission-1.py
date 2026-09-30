class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        candidates.sort()
        def backtrack(curr, curr_sum, idx):

            if curr_sum == target:
                ans.append(curr[:])

            if curr_sum >= target:
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                if curr_sum + candidates[i] > target:
                    break

                curr_sum += candidates[i]
                curr.append(candidates[i])
                
                backtrack(curr, curr_sum, i + 1)

                curr_sum -= candidates[i]
                curr.pop()
                    
        
        backtrack([], 0, 0)
        return ans