class Solution(object):
    def intersection(self, nums1, nums2):
        l=[]
        d1={}
        d2={}
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
                l.append(i)
        return l        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        