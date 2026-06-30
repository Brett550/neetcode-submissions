class MedianFinder:

    def __init__(self):
        self.nums = []
        self.length = 0

        

    def addNum(self, num: int) -> None:
        print("adding", num)
        self.nums.append(num)
        self.length += 1
        self.nums.sort()
        

    def findMedian(self) -> float:
        print(self.length)
        if self.length % 2 == 0:
            middle = self.length // 2
            lower = middle - 1
            higher = middle #math.ceil(middle)
            # print("lower",lower)
            # print("higher",higher)
            return (self.nums[lower] + self.nums[higher]) / 2
        if self.length % 2 != 0:
            middle = self.length // 2
            return self.nums[middle]
        
        