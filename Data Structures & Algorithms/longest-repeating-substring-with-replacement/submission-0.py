class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # O(mn) solution below
        maxLength = 0
        charSet = set(s)

        for char in charSet:
            left = 0
            matchCount = 0
            for right in range(len(s)):
                if s[right] == char:
                    matchCount += 1
                while right - left + 1 - matchCount > k:
                    if s[left] == char:
                        matchCount -= 1
                    left += 1 
                maxLength = max(maxLength, right - left + 1)

        return maxLength
                
            
            
        
                
                

            





