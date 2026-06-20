class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_list = sorted(list(set(nums)))
        # print(sorted_list)
        max_length = -1
        length = 1
        for i in range(1, len(sorted_list)):
            if sorted_list[i] != (sorted_list[i-1]+1):
                max_length = max(max_length, length)
                # print("max_length is now", max_length)
                length = 1
            else:
                length +=1
                # print(sorted_list[i], "is 1 more than",sorted_list[i-1])
        max_length = max(max_length,length)
        return max_length