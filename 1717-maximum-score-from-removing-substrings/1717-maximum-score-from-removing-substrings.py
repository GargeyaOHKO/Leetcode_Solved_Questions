class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x>=y:
            w='ab'
            p1,p2=x,y
        else:
            w='ba'
            p1,p2=y,x
        r,total=0,0
        stack=[]
        for i in s:
            stack.append(i)
            if len(stack)>1 and stack[-2]==w[0] and stack[-1]==w[1]:
                total+=p1
                stack.pop()
                stack.pop()
        s="".join(stack)
        print(s)
        stack=[]
        for i in s:
            stack.append(i)
            if len(stack)>1 and stack[-2]==w[1] and stack[-1]==w[0]:
                total+=p2
                stack.pop()
                stack.pop()
        return total
                
        