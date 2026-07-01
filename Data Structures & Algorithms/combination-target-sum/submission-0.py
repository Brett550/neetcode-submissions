class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answers = []
        
        def backtrack(start, cur_com):
            if sum(cur_com) == target:
                answers.append(list(cur_com)) #append deep copy
                return
            elif sum(cur_com) > target: #stop search once it is irrelevant
                return
            for i in range(start, len(nums)):
                #add element
                cur_com.append(nums[i])

                #explore
                backtrack(i, cur_com)

                # unchoose
                cur_com.pop()

        backtrack(0, [])
        return answers
        