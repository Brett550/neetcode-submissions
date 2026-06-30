class MedianFinder:

    def __init__(self):
        self.nums = []
        self.length = 0

        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.length += 1
        self.nums.sort()
        

    def findMedian(self) -> float:
        if self.length % 2 == 0:
            middle = self.length // 2
            lower = middle - 1
            higher = middle #math.ceil(middle)
            return (self.nums[lower] + self.nums[higher]) / 2
        if self.length % 2 != 0:
            middle = self.length // 2
            return self.nums[middle]
        
        