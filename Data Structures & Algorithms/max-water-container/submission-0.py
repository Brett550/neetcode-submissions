class Solution:
    def maxArea(self, heights: List[int]) -> int:
    
        left = 0
        right = len(heights)-1
        max_area = 0

        while(left < right):
            smaller = min(heights[left], heights[right])
            area = smaller * (right-left)

            max_area = max(max_area, area)

            if(smaller == heights[left]):
                left += 1
            if(smaller == heights[right]):
                right -= 1
        return max_area

