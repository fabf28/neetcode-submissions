class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #brute force + two pointer
        l = 0
        r = 1
        n = len(s)

        if n == 0 or n == 1:
            return n

        maxLength = 1
        maxString = s[0]
        chars = dict()
        self.addChar(chars, s[0])
        self.addChar(chars, s[1])
        m = 2

        while r < n:
            sub = s[l: r + 1]
            if not self.noDuplicate(chars, sub[-1]):
                if m > maxLength:
                    maxString = sub
                    maxLength = m
                    r += 1
                    m += 1
                    if r < n:
                        self.addChar(chars, s[r])
                else:
                    r += 1
                    m += 1
                    if r < n:
                        self.addChar(chars, s[r])
            else:
                while s[r] != s[l]:
                    chars[s[l]] -= 1
                    l += 1
                    m -= 1
                chars[s[l]] -= 1
                l += 1
                r += 1
                if r < n:
                    self.addChar(chars, s[r])
        print(maxString)
        return maxLength

    
    def noDuplicate(self, dict1, char):
        if char not in dict1:
            return False
        elif dict1[char] == 0 or dict1[char] == 1:
            return False
        else: 
            return True
    
    def addChar(self, dict1, char):
        if char not in dict1:
            dict1[char] = 1
        else:
            dict1[char] += 1
