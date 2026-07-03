class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for myStr in strs:
            length = str(len(myStr))
            encoded.append(length)
            encoded.append('#')
            encoded.append(myStr)

        # print(''.join(encoded))
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        answer = []
        curWord = []
        digit = []
        strLength = 0
        i = 0
        while i < len(s):
            # inner loop to parse number
            while s[i] != '#':
                digit.append(s[i])
                i += 1
            if s[i] == '#':
                strLength = int(''.join(digit))
                i += 1
            for j in range(strLength):
                curWord.append(s[i])
                i += 1
            answer.append(''.join(curWord))
            curWord = []
            digit = []
        return answer



