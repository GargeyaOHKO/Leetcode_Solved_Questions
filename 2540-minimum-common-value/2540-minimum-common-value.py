class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        d1={}
        d2={}
        minnum=9999999999
        for i in nums1:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1    
        for i in nums2:
            if i not in d2:
                d2[i]=1
            else:
                d2[i]+=1
        for i in d1:
            if i in d2:
                minnum=min(minnum,i)            
        if minnum==9999999999:
            return -1
        return minnum        
        