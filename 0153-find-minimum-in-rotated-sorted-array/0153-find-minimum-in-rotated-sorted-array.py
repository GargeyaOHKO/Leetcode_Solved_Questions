class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,n-1
        #print(nums)
        while l<=r:
            mid=(r+l)//2
            if mid!=0 and mid!=len(nums)-1:
                if nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
                    return nums[mid]
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid-1
                c=nums[mid]
        return c