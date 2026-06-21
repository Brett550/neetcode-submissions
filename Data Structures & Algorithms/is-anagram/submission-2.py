class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_counts = Counter(s)
        # t_counts = Counter(t)

        # return s_counts == t_counts

        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))

        return hash(sorted_s) == hash(sorted_t)


