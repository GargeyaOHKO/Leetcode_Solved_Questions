class Solution(object):
    def numberOfSubarrays(self, nums, k):
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0   #Even=0
            else:
                nums[i]=1   #Odd=1
        d={0:1}
        maxc=0
        r=0
        c=0
        while r<len(nums):
            c+=nums[r]
            if c-k in d:
                maxc+=d[c-k]
            if c in d:
                d[c]+=1
            else:
                d[c]=1
            r+=1    
        return maxc        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """