class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # o(n) solution
        if len(nums) == 0:
            return 0
        
        longest_streak = 1
        #put all nums into a hash
        my_set = set(nums)

        # check
        for num in my_set:
            if num-1 in my_set:
                continue
            else: #looking at start of sequence
                cur = num
                streak = 1
                while(cur+1 in my_set):
                    streak += 1
                    cur += 1
                    longest_streak = max(longest_streak, streak)
        return longest_streak
        
        # below is o(nlogn) solution
        # if len(nums) == 0:
        #     return 0

        # sorted_list = sorted(list(set(nums)))
        # max_length = -1
        # length = 1
        # for i in range(1, len(sorted_list)):
        #     if sorted_list[i] != (sorted_list[i-1]+1):
        #         max_length = max(max_length, length)
        #         length = 1
        #     else:
        #         length +=1
        # max_length = max(max_length,length)
        # return max_length