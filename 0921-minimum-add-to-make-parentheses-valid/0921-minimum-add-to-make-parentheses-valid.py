class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ob=0
        cb=0
        for i in s:
            if i=='(':
                ob+=1
            elif i==')' and ob>0:
                ob-=1
            elif i==')' and ob==0:
                cb+=1
        return abs(ob+cb)
        
        
        