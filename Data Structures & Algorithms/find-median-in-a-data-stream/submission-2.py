class MedianFinder:

    def __init__(self):
        self.mini = []
        self.maxi = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxi, num * -1)#maxheap
        if self.maxi and self.mini and self.maxi[0] * -1 > self.mini[0]:
            popped = heapq.heappop(self.maxi) * -1
            heapq.heappush(self.mini, popped)
        if len(self.mini) - len(self.maxi) >= 2:
            popped = heapq.heappop(self.mini) * -1
            heapq.heappush(self.maxi, popped)
        if len(self.maxi) - len(self.mini) >= 2:
            popped = heapq.heappop(self.maxi) * -1
            heapq.heappush(self.mini, popped)

    def findMedian(self) -> float:
        if len(self.mini) > len(self.maxi):
            return self.mini[0]
        if len(self.maxi) > len(self.mini):
            return self.maxi[0] * -1
        return ((self.maxi[0] * -1) + self.mini[0]) / 2