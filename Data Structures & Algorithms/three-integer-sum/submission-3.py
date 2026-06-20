class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: #check for dupe i
                continue
            left = i+1
            right = len(nums)-1
            while(left < right):
                if nums[left] + nums[right] == -nums[i]:
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]: #check for dupe left
                        left += 1
                    while left < right and nums[right] == nums[right + 1]: #check for dupe right
                        right -= 1


                if nums[left] + nums[right] < -nums[i]:
                    left += 1
                if nums[left] + nums[right] > -nums[i]:
                    right -= 1
        return answer