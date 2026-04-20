class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        def isAlpha(c):
            if 'a' <= c <= 'z' or 'A' <= c <= 'Z' or c.isdigit():
                return True
            return False

        front, back = 0, len(s)-1
        while front <= back:
            c1, c2 = s[front], s[back]
            if not isAlpha(c1):
                front += 1
                continue
            if not isAlpha(c2):
                back -= 1
                continue
            
            if s[front] != s[back]:
                return False
            front += 1
            back -= 1
        return True
        