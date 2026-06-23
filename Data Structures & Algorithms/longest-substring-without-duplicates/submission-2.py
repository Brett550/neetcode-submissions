class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        left = 0
        curString = ''
        length = 0
        maxLength = -1

        for right in range(len(s)):
            newChar = s[right]
            print(newChar, "is newChar")
            print(curString, "is curString")

            while newChar in curString:
                print(newChar, "found in", curString)
                curString = curString.replace(s[left], '', 1)
                left += 1
                length -= 1

            length += 1
            # print(length, "is length")
            maxLength = max(length, maxLength)

            curString += s[right]
            # curString = curString.join(s[right]) INCORRECT, join connects an array of strings

        return maxLength

