class Solution:
    def isPalindrome(self, s: str) -> bool:
        fixed = re.sub(r"[^a-zA-Z0-9]+", '', s)
        fixed = fixed.strip()
        fixed = fixed.lower()

        left = 0
        right = len(fixed)-1

        while(left <= right):
            if fixed[left] != fixed[right]:
                return False
            left += 1
            right -= 1
        return True

        # return fixed == fixed[::-1]