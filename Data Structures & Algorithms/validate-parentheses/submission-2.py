class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        } 

        for c in s:
            if c in match.values():
                stack.append(c)
            else:
                if not stack or stack[-1] != match[c]:
                    return False
                stack.pop()

        return not stack
        