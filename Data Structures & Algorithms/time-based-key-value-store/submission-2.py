from collections import defaultdict

class TimeMap:

    hm = defaultdict(list)

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # First we grab the list

        key_list: list = self.hm.get(key, [])

        # Attempt to find the insert point

        if len(key_list) == 0:
            key_list.append((timestamp, value))
            self.hm[key] = key_list
            return

        l, r = 0, len(key_list) - 1

        while l <= r:

            mid = (l + r) // 2

            if key_list[mid][0] == timestamp:
                key_list.insert(mid, (timestamp, value))
                self.hm[key] = key_list
                return
            
            if key_list[mid][0] < timestamp:
                r = mid - 1
            else:
                l = mid + 1

        key_list.insert(l, (timestamp, value))

        self.hm[key] = key_list



    def get(self, key: str, timestamp: int) -> str:
        key_list: list = self.hm.get(key, [])
        
        if len(key_list) == 0:
            return ""

        l, r = 0, len(key_list) - 1

        while l <= r:

            mid = mid = (l + r) // 2


            if key_list[mid][0] == timestamp:
                
                return key_list[mid][1]
            
            if key_list[mid][0] < timestamp:
                r = mid - 1
            else:
                l = mid + 1
        
        if l > len(key_list) - 1:
            return ""

        if key_list[l][0] <= timestamp:

            return key_list[l][1]
        else:
            return ""
