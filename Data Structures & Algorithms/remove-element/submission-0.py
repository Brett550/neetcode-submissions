class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        keep = []
        answer = []
        for num in nums:
            if num == val:
                keep.append(num)

        for num in keep:
            nums.remove(num) #remove val occurences from list
        # print(nums)
        
        return len(nums)