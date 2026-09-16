class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        mini = 1
        maxi = max(piles)

        def check_function(try_num: int) -> bool:
            curr_count = 0
            for pile in piles:
                # get the amount of hours
                curr_count += math.ceil(pile / try_num)

            if curr_count > h:
                return False
            
            return True

        ans = maxi
        while mini <= maxi:
            mid = (mini + maxi) // 2

            if not check_function(mid):
                mini = mid + 1
            else:
                ans = min(ans, mid)
                maxi = mid - 1
        
        # placeholder since above should return
        return ans

