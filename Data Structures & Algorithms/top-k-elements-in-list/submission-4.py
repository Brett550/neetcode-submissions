class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)

        buckets = [[None] for x in range(len(nums)+1)]

        for element, freq in frequencies.items():
            buckets[freq].append(element)

        count = 0
        answer = []
        for arr in reversed(buckets):
            if count >= k:
                break
            for num in arr:
                if num is None:
                    continue
                else:
                    answer.append(num)
                    count += 1

        return answer
