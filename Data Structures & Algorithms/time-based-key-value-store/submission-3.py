class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if self.map:
            if (key, timestamp) in self.map:
                return self.map[(key, timestamp)]
            else:
                retKey, retTime = 0, float('-inf')
                found = False
                for pair in self.map:
                    if pair[0] == key and pair[1] <= timestamp:
                        found = True
                        retTime = max(retTime, pair[1])
                        retKey = pair[0]
                if found:
                    return self.map[(retKey, retTime)]
                else:
                    return ""
        else:
            return ""