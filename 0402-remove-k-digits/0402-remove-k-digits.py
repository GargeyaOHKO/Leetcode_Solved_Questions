class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num+="0"
        stack=[]
        for i in num:
            while stack and stack[-1]>i and k>0:
                stack.pop()
                k-=1
            if not stack:
                stack.append(i)
            elif stack and stack[-1]<i:
                stack.append(i)
            else:
                stack.append(i)
        stack.pop()
        s=""
        for i in stack:
            s+=i
        s=s.lstrip('0')
        if not s:
            return "0"
        return s.lstrip('0')