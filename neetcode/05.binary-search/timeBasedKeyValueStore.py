class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ''
        values = self.map.get(key, []) # timestamps are strickly increasing, so we don't need to sort
        
        l, r = 0, len(values) - 1
        while l <= r:
            m = l + (r - l) // 2
            if values[m][1] <= timestamp:
                ans = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)