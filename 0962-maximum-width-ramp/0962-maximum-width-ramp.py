class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        l=[]
        m=float('-inf')
        for i in range(len(nums)-1,-1,-1):
            m=max(m,nums[i])
            l.insert(0,m)
        #print(l)
        left,right=0,1
        maxlen=0
        while right<len(nums):
            if l[right]>=nums[left]:
                maxlen=max(maxlen,right-left)
                right+=1
            elif l[right]<nums[left]:
                left+=1
        return maxlen
