class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        if len(self.arr) % 2 == 0:
            midL, midR = math.floor((len(self.arr)-1)/2), math.ceil((len(self.arr)-1)/2)
            return (self.arr[midL] + self.arr[midR]) / 2
        else:
            return self.arr[math.floor((len(self.arr)-1)/2)]