class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r=0,max(nums)
        def slide(mid):
            l,r=0,1
            c=0
            while r<len(nums):
                while nums[r]-nums[l]>mid:
                    l+=1
                c+=r-l
                r+=1
            return c
        while l<r:
            mid=l+((r-l)//2)
            res=slide(mid)
            if res>=k:
                r=mid
            else:
                l=mid+1
        return l
