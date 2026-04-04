class Solution:
    def isValid(self, s: str) -> bool:
        close_open_mapping = {")": "(" , "]": "[", "}": "{"}
        stack = []

        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in close_open_mapping:
                if stack and stack[-1] == close_open_mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if len(stack) > 0:
            return False
        else:
            return True

        