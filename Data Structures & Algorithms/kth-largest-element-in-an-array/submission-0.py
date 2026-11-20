class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        #load the heap
        for num in nums:
            heapq.heappush(heap, num*-1)

        #find kth largest
        answer = 0
        for i in range(k):
            answer = heapq.heappop(heap)
        return answer*-1