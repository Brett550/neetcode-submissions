class Solution:
    def isPalindrome(self, s: str) -> bool:
        fixed = re.sub(r"[^a-zA-Z0-9]+", '', s)
        # print(fixed)
        fixed = fixed.strip()
        fixed = fixed.lower()
        return fixed == fixed[::-1]