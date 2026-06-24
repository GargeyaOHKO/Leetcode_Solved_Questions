class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s=set()
        res=[]
        for i in range(len(A)): 
            s.add(A[i])
            c=0
            for j in range(i+1): 
                if B[j] in s:
                    c+=1
            res.append(c) 
        return res