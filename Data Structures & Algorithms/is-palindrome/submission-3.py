class Solution:
    def isPalindrome(self, s: str) -> bool:
        #2n complexity - two pass
        s = s.lower()
        l = 0
        r = len(s) - 1

        while r > l:
            while s[l].isalnum() == False and r > l:
                l += 1
            while s[r].isalnum() == False and r > l:
                r -= 1
            if s[l] != s[r]:
                print(s[l], s[r])
                return False
            l += 1
            r -= 1
        return True

        