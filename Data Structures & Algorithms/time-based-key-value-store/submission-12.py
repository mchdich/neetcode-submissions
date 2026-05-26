class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
    # store = {
    #   "alice": [[1, "happy"], [2, "sad"]]
    # }
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not self.store or key not in self.store:
            return ""
        maxTS, retIdx = -1, -1
        for i in range(len(self.store[key])):
            if self.store[key][i][0] <= timestamp:
                maxTS = self.store[key][i][0]
                retIdx = i
        return self.store[key][retIdx][1] if maxTS > -1 and retIdx > -1 else ""