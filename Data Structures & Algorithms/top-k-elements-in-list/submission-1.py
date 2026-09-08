from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hm = defaultdict(int)
        heap = []
        heapq.heapify(heap)

        for num in nums:
            hm[num] += 1

        for key, v in hm.items():
            heapq.heappush(heap, (-v, key))
        
        ans = []
        for i in range(k):
            if len(heap) == 0:
                return ans

            num_tuple = heapq.heappop(heap)
            
            ans.append(num_tuple[1])

        return ans
