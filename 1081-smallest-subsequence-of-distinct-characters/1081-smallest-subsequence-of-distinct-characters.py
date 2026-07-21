class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last={}
        for i in range(len(s)-1,-1,-1):
            if s[i] not in last:
                last[s[i]]=i
        stack=[]
        for i in range(len(s)):
            while stack and ord(stack[-1])>ord(s[i]) and last[stack[-1]]>i and s[i] not in stack:
                stack.pop()
            if s[i] not in stack:
                stack.append(s[i])
        return "".join(stack)


