class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix product
        prefix = []
        lastNum = 1
        for num in nums:
            mySum = num * lastNum
            lastNum = mySum
            prefix.append(mySum)
        print(prefix)


        #postfix product
        suffix = []
        lastNum = 1
        for num in reversed(nums):
            mySum = num * lastNum
            lastNum = mySum
            suffix.append(mySum)
        print(suffix)


        #calculation
        answer= []
        revSuf = suffix[::-1]
        # left = 1
        for i in range(len(prefix)):
            leftNum = 0
            rightNum = 0
            if i-1 < 0:
                leftNum = 1
            else:
                leftNum = prefix[i-1]
            if i+1 > len(prefix)-1:
                rightNum = 1
            else:
                rightNum = revSuf[i+1]
            
            answer.append(leftNum*rightNum)

        return answer