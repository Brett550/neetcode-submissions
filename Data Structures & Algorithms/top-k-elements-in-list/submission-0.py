class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        answer = []
        for item, count in counts.most_common(k):
            answer.append(item)
        return answer