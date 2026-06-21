class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            calc = target - num
            # print(i, num)
            if calc in seen:
                return [seen[calc], i]
            else:
                seen[num] = i
                # print("Adding key", calc, "and value", i)
        return []

