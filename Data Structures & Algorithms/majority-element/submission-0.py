class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elments = Counter(nums)
        most_common = elments.most_common(1)[0] #get most common num + count touple
        num, freq = most_common

        return num