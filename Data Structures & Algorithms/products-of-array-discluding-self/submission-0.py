class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product = math.prod(nums)
        # answer = []
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         answer.append(product)
        #     else:
        #         answer.append(product//nums[i])
        # return answer

        #get prefix product
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(nums[i] * prefix[len(prefix)-1])
        print(prefix)

        #get suffix product
        suffix = []
        for i, item in reversed(list(enumerate(nums))):
            if i == len(nums)-1:
                suffix.append(item)
            else:
                suffix.append(item * suffix[len(suffix)-1])
        suffix = suffix[::-1]
        print(suffix)
        
        #find final answer
        answer = []
        for i in range(len(suffix)):
            leftIndex = i-1
            rightIndex = i+1
            leftNum = 0;
            rightNum = 0;
            if leftIndex < 0:
                leftNum = 1
            else:
                leftNum = prefix[leftIndex]

            if rightIndex > len(nums)-1:
                rightNum = 1
            else:
                rightNum = suffix[rightIndex]
            
            answer.append(leftNum*rightNum)
            
        return answer


        