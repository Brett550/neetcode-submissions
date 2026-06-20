class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        answer = []
        for word in strs:
            mySorted = ''.join(sorted(word)) #need the join since sorted returns list of individual chars
            groups[mySorted].append(word)
        for group in groups.values(): #values since getting actual string, not sorted one
            answer.append(group)
        return answer