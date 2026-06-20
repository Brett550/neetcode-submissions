class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        
        for item, count in counts.items():
            if count > 1:
                return True
        return False