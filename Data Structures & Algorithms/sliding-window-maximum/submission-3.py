
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # initial approach: we can use a heap to track the max and then pop off the left since this is a fixed window size

        heap = []

        left = 0
        ans = []

        for right in range(len(nums)):

            heapq.heappush(heap, (-nums[right], right))

            while right - left + 1 > k:
                left += 1


            if right - left + 1 == k:
                curr_max = heap[0]
                while curr_max[1] < left:
                    heapq.heappop(heap)
                    curr_max = heap[0]
                
                ans.append(-curr_max[0])
        
        return ans