class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        c=0
        for i in range(len(nums)):
            d={}
            for j in range(i,len(nums)):
                d[nums[j]]=d.get(nums[j],0)+1
                if target in d and d[target]>(j-i+1)//2:
                    c+=1
        return c