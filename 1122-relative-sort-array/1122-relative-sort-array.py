class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d={}
        l1=[]
        l2=[]
        for i in arr1:
            if i in arr2:
                d[i]=d.get(i,0)+1
            else:
                l2.append(i)    
        for i in range(len(arr2)):
            for j in range(d[arr2[i]]):
                l1.append(arr2[i])
        l2.sort()        
        return l1+l2