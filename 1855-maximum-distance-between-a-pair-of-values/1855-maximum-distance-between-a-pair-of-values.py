class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i,j=len(nums1)-1,len(nums2)-1
        maxi=0
        while i>-1:
            #print(i,j)
            if nums1[i]<=nums2[j]:
                maxi=max(maxi,j-i)
                i-=1
            elif nums1[i]>nums2[j] and i<j:
                j-=1
            elif nums1[i]>nums2[j] and i==j:
                i-=1
                j-=1
            elif nums1[i]>nums2[j] and i>j:
                i-=1
        return maxi

                