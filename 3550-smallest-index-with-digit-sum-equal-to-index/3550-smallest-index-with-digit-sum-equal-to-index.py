class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            curr=nums[i]
            s=0
            while curr>0:
                s+=curr%10
                curr=curr//10
            if s==i:
                return i
        return -1