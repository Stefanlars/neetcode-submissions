class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_min = None

        for i in range(len(prices)):

            if curr_min is not None:
                
                max_profit = max(max_profit, prices[i] - curr_min)

                curr_min = min(curr_min, prices[i])
            else:
                curr_min = prices[i]
        
        return max_profit