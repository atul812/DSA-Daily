class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i not in ['+', '-', '*','/']:
                stk.append(int(i))
            else:
                val2 = stk.pop()
                val1 = stk.pop()
                if i == "+":
                    ans = val1 + val2
                elif i == "-":
                    ans = val1 - val2
                elif i == "*":
                    ans = val1 * val2
                elif i == "/":
                    ans = int(val1 / val2)
                stk.append(ans)
        return stk[-1]
