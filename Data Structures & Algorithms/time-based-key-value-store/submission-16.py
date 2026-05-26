class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
    # store = {
    #   "alice": [[1, "happy"], [2, "sad"], [5, "neutral"]]
    # }
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not self.store or key not in self.store:
            return ""
        maxTS, retIdx = -1, -1
        l, r = 0, len(self.store[key])
        while l < r:
            m = (l+r)//2
            if self.store[key][m][0] > timestamp:
                r = m
            elif self.store[key][m][0] <= timestamp:
                maxTS = self.store[key][m][0]
                retIdx = m
                l = m + 1
            else:
                return self.store[key][m][1]
        return self.store[key][retIdx][1] if maxTS > -1 and retIdx > -1 else ""