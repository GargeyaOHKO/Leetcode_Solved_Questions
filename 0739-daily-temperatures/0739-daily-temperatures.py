class Solution(object):
    def dailyTemperatures(self, t):
        l=[0]*len(t)
        stack=[]
        for i in range(len(t)-1):
            if t[i]<t[i+1]:
                l[i]=1
                c=0
                while stack and stack[-1][0]<t[i+1]:
                    x=stack.pop()
                    l[x[1]]=i+1-(x[1])
            else:
                stack.append([t[i],i])
        return l
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        