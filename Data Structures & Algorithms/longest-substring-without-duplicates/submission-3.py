class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #brute force + two pointer
        

        l = 0
        r = 1
        n = len(s)

        if n == 0:
            return 0

        maxLength = 1
        maxString = s[0]
        m = 2

        while r < n:
            sub = s[l: r + 1]
            print(m, sub)
            if self.noDuplicate(sub):
                if m > maxLength:
                    maxString = sub
                    maxLength = m
                    r += 1
                    m += 1
                else:
                    r += 1
                    m += 1
            else:
                while s[r] != s[l]:
                    l += 1
                    m -= 1
                l += 1
                r += 1
        return maxLength

            

    
    def noDuplicate(self, string):
        chars = []
        for c in string:
            if c in chars:
                return False
            else:
                chars.append(c)
        return True