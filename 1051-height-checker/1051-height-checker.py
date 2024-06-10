class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        l=[0]*101
        for i in heights:
            l[i]+=1
        c=0
        i,j=0,0
        while i<len(heights):
            if l[j]==0:
                j+=1
            elif l[j]>0:
                for k in range(l[j]):    
                    if heights[i]!=j:
                        c+=1
                        i+=1
                    else:
                        i+=1
                j+=1            
        return c






        