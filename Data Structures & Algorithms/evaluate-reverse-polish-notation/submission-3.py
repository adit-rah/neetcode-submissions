class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        exp = []
        for t in tokens:
            if t not in "+-*/":
                exp.append(int(t))
            else:
                b = exp.pop()
                a = exp.pop()

                if t == "+":
                    exp.append(a + b)
                elif t == "-":
                    exp.append(a - b)
                elif t == "*":
                    exp.append(a * b)
                else:
                    exp.append(int(a / b))
        
        return exp[-1]
            

            

        