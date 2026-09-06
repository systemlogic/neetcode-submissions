class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for ch in tokens:
            if ch not in ["+", "-", "*", "/"]:
                stk.append(int(ch))

            else:
                num_2 = stk.pop()
                num_1 = stk.pop()
                
                if ch == "*":
                    stk.append(num_1 * num_2)
                elif ch == "/":
                    stk.append(int(num_1 / num_2))
                elif ch == "+":
                    stk.append(num_1 + num_2)
                elif ch == "-":
                    stk.append(num_1 - num_2)
        return stk[-1]