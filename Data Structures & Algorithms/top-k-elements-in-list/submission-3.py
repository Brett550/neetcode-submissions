class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums).items()

        buckets = [[] for _ in range(len(nums) + 1)] #add 1 to prevent out of range, lists since numbers can have same freq

        for num, freq in freqs:
            buckets[freq].append(num)

        
        answer = []
        count = 0
        for lists in reversed(buckets):
            for num in lists:
                if num is None:
                    continue
                if count >= k:
                    break
                else:
                    answer.append(num)
                    count += 1
        return answer
