class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        answer = []
        
        #go thru and hash stuff
        for i in range(len(strs)):
            my_str = strs[i]
            sortedStr = ''.join(sorted(strs[i]))

            curHash = hash(sortedStr)
            groups[sortedStr].append(my_str)
        
        for k, v in groups.items():
            answer.append(v)
        return answer