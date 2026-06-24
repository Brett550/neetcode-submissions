class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')' or char == '}' or char == ']':
                try:
                    popped = stack.pop()
                except:
                    return False

                if popped == '(' and char != ')':
                    return False
                elif popped == '[' and char != ']':
                    return False
                elif popped == '{' and char != '}':
                    return False

        if len(stack) != 0:
            return False
        return True