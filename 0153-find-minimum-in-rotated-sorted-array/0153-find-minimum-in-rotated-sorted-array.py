class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,n-1
        #print(nums)
        while l<=r:
            mid=(r+l)//2
            #print(mid)
            #print(nums[(mid-1)%n], nums[mid], nums[(mid+1)%n])
            if nums[mid]<=nums[(mid+1)%n] and nums[mid]<=nums[(mid-1)%n]:
                return nums[mid]
            elif nums[mid]<nums[(mid+1)%n] and nums[mid]>nums[(mid-1)%n]:
                r=mid-1
            elif nums[mid]>nums[(mid+1)%n] and nums[mid]<nums[(mid-1)%n]:
                l=mid+1
            else:
                if nums[(mid+1)%n]<nums[(mid-1)%n]:
                    return nums[(mid+1)%n]
                else:   
                    return nums[(mid-1)%n]
        
        l,r=0,n-1
        #print(nums)
        while l<=r:
            mid=(r+l)//2
            #print(mid)
            #print(nums[(mid-1)%n], nums[mid], nums[(mid+1)%n])
            if nums[mid]<=nums[(mid+1)%n] and nums[mid]<=nums[(mid-1)%n]:
                return nums[mid]
            elif nums[mid]<nums[(mid+1)%n] and nums[mid]>nums[(mid-1)%n]:
                l=mid+1
            elif nums[mid]>nums[(mid+1)%n] and nums[mid]<nums[(mid-1)%n]:
                r=mid-1
            else:
                if nums[(mid+1)%n]<nums[(mid-1)%n]:
                    return nums[(mid+1)%n]
                else:   
                    return nums[(mid-1)%n]
