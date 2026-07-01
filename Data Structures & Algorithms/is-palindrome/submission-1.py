class Solution:
    def isPalindrome(self, s: str) -> bool:
        #2n complexity - two pass
        s = [x for x in s.lower() if x.isalnum() == True]
        l = 0
        r = len(s) - 1
        print(s)

        while r > l:
            if s[l] != s[r]:
                print(s[l], s[r])
                return False
            l += 1
            r -= 1
        return True

        