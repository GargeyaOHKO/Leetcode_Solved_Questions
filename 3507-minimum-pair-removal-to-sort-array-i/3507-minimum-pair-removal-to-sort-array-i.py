class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans=0
        while True:
            temp=nums[:]
            temp.sort()
            if nums==temp:
                return ans
            else:
                smol=float('inf')
                index=-1
                for i in range(len(nums)-1):
                    if nums[i]+nums[i+1]<smol:
                        smol=nums[i]+nums[i+1]
                        index=i
                #print(smol,index)
                newl=[]
                for i in range(len(nums)):
                    if i==index:
                        newl.append(smol)
                    elif i==index+1:
                        a=1
                    else:
                        newl.append(nums[i])
                ans+=1
                nums=newl[:]
                #print(nums)
        