class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        diff=float('inf')
        num=float('inf')
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            #print(nums[i],nums[l],nums[r])
            while l<r:
                print(nums[i],nums[l],nums[r],)
                if nums[i]+nums[l]+nums[r]==target:
                    return target
                if abs((nums[i]+nums[l]+nums[r])-target)<diff:
                    print("swap")
                    diff=abs((nums[i]+nums[l]+nums[r])-target)
                    num=(nums[i]+nums[l]+nums[r])
                if (nums[i]+nums[l]+nums[r])-target>0:
                    r-=1
                else:
                    l+=1
        return num 
            
        