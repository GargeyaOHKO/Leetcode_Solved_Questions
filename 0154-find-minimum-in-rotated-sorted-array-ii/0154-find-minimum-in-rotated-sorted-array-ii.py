class Solution:
    def findMin(self, nums: List[int]) -> int:
        def dc(left,right):
            if left==right:
                return nums[left]
            mid=(left+right)//2
            return min(dc(left,mid),dc(mid+1,right))
        return dc(0,len(nums)-1)