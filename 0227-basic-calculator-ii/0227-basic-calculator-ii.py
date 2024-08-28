class Solution:
    def calculate(self, s: str) -> int:
        num,sign,stack=0,"+",[]
        for i in s+"+":
            print(stack)
            if i.isdigit():
                num=num*10+int(i)
            elif i in "+-*/":
                if sign=='+':
                    stack.append(num)
                elif sign=='-':
                    stack.append(-num)
                elif sign=='*':
                    stack.append(stack.pop()*num)
                else:
                    stack.append(math.trunc(stack.pop()/num))
                sign=i
                num=0
        return sum(stack)

        