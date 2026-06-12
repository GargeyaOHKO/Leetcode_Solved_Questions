class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        asum,dsum=0,0
        flag=True
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                asum+=nums[i]
            else:
                if flag:
                    asum+=nums[i]
                    flag=False
                dsum+=nums[i]
        dsum+=nums[-1]
        #print(asum,dsum)
        if asum>dsum:
            return 0
        elif dsum>asum:
            return 1
        else:
            return -1