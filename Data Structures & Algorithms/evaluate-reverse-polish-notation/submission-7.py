class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        opps = ["+", "-", "/", "*"]
        stack = []

        for x in tokens:
            if x in opps:
                a = stack.pop()
                b = stack.pop()
                if x == "+":
                    res = a + b
                elif x == "*":
                    res = a * b
                elif x == "/":
                    res = int(b / a)
                elif x == "-":
                    res = b - a
                stack.append(res)
            else:
                stack.append(int(x))
        
        return (stack[-1])