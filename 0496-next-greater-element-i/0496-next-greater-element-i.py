class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in nums1:
            flag=False
            maxi=-1
            for j in range(len(nums2)):
                if i==nums2[j]:
                    flag=True
                if flag and nums2[j]>i:
                    maxi=nums2[j]
                    l.append(nums2[j])
                    break
            if flag==False or maxi==-1:
                l.append(-1)
        return l           