class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]==')':
                arr=[]
                while stack[-1]!='(':
                    arr.append(stack.pop())
                stack.pop()
                stack.extend(arr)    
            else:
                stack.append(s[i])
        #print(stack)
        return "".join(stack)
        

