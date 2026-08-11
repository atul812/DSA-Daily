class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for i in range(len(operations)):
            if operations[i] == "C":
                stk.pop()
            elif operations[i] == "D":
                stk.append(stk[-1]*2)
            elif operations[i] == "+":
                stk.append(stk[-1]+stk[-2])
            else:
                stk.append(int(operations[i]))

        sum = 0
        for j in range(len(stk)):
            sum += stk[j]

        return sum
