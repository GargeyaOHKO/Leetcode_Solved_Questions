class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d={}
        for i in range(len(s)-1,-1,-1):
            if s[i] not in d:
                d[s[i]]=i
        #print(d)
        i=0
        stack=[]
        while i<len(s):
            while stack and ord(stack[-1])>ord(s[i]) and d[stack[-1]]>i and s[i] not in stack:
                stack.pop()
            if s[i] not in stack:
                stack.append(s[i])
            i+=1
        return "".join(stack)
