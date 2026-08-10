class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answers = []
        firstWord = ""
        if len(strs) != 0 and len(strs[0]) != 0:
            firstWord = strs[0]
        if len(strs) == 1:
            return strs[0]

        for word in strs[1:]:
            print("Current answer is")
            index = 0
            prefix = ""
            print("Prefix for index", index, "for word", word, "is", prefix)
            for letter in word:
                if 0 <= index < len(firstWord):
                    if firstWord[index] == letter:
                        print(letter)
                        print(firstWord[index])
                        prefix += letter
                        index += 1
                else:
                    print("final prefix was", prefix)
                    break
            answers.append(prefix)

            shortest_string = min(answers, key=len)
            if len(shortest_string) == 0:
                shortest_string == ""

            # if answer != prefix:
            #     if len(prefix) >= len(answer):
            #         answer = prefix

        return shortest_string