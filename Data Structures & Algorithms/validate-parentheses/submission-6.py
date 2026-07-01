class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        stack = []
        s = list(s)
        while len(s) > 0:
            off = s.pop(0)
            if off in brackets:
                stack.append(off)
            elif stack == []:
                return False
            elif brackets[stack[-1]] == off:
                stack.pop(-1)
            else:
                return False
        print("stack: ", stack)
        print("s: ", s)
        if stack == [] and s == []:
            return True
        return False