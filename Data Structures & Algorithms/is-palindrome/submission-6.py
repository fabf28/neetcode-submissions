class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s.lower() if c.isalnum()])
        n = len(s)
        l = 0
        r = n - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            r -= 1
            l += 1
        return True

        