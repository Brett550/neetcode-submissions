class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        answer = nums[0]
        while left <= right:
            if nums[left] < nums[right]: #whole thing sorted
                answer = min(answer, nums[left])
                break

            #calculate middle
            mid = (left + right) // 2
            answer = min(answer, nums[mid])
            if nums[mid] >= nums[left]: #left half sorted, move search to right half
                left = mid + 1
            else: #search in left half
                right = mid - 1
        return answer

