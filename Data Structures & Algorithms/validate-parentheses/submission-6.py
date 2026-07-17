class Solution:
    def isValid(self, s: str) -> bool:
        close = set([')','}',']']) 
        match = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        stack = []

        for c in s:
            if c in close:
                if not stack or stack[-1] != match[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return not stack