class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        c=1
        for i in range(len(nums)-1):
            if nums[i]!=c:
                return False
            c+=1
        if nums[len(nums)-1]==(c-1):
            return True
        return False