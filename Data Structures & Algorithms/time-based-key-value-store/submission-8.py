class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if not self.map:
            return ""
        if (key, timestamp) in self.map:
            return self.map[(key, timestamp)]
        maxKey, maxTime = 0, -1
        found = False #key, ts not guaranteed
        for pair in self.map:
            if pair[0] == key and pair[1] <= timestamp:
                found = True
                maxTime = max(maxTime, pair[1])
                maxKey = pair[0]
        if found:
            return self.map[(maxKey, maxTime)]
        return ""