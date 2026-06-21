class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        answer = []

        freqs = counts.most_common(k)

        for num, count in freqs:
            answer.append(num)

        return answer
