class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #O(n) solution
        counts = {} #to count frequencies of letters in window
        left = 0
        maxFreq = 0 #letter in window with highest frequency
        maxLength = 0
        for right in range(len(s)):
            counts[s[right]] = 1 + counts.get(s[right],0) #update frequency with new letter
            maxFreq = max(maxFreq, counts[s[right]]) #update max frequency

            if (right - left + 1) - maxFreq > k: #if # infrequent letters > k, shrink the window
                if counts[s[left]] > 0:
                    counts[s[left]] = counts.get(s[left]) - 1
                left += 1
            maxLength = max(maxLength, right - left +1)
        return maxLength

        
        
        # # O(mn) solution below
        # maxLength = 0
        # charSet = set(s)

        # #for each character in s, see how many of them there are and if non matching > k shrink window
        # for char in charSet:
        #     left = 0
        #     matchCount = 0
        #     for right in range(len(s)):
        #         if s[right] == char:
        #             matchCount += 1
        #         while right - left + 1 - matchCount > k:
        #             if s[left] == char:
        #                 matchCount -= 1
        #             left += 1 
        #         maxLength = max(maxLength, right - left + 1)

        # return maxLength
                
            
            
        
                
                

            





