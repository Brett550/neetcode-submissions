class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        mySet = set(nums)

        maxLength = float('-inf')
        for num in mySet:
            if num-1 in mySet:
                continue
            else:
                cur = num
                length = 1
                while cur+1 in mySet:
                    length += 1
                    cur = cur+1
                maxLength = max(length, maxLength)
        return maxLength


        