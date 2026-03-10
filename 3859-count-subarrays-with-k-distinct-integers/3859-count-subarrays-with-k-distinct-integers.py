class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        totalnum=0
        d1,d2={},{}
        r1,r2=-1,-1
        totalc=0
        for l in range(len(nums)):
            print(l,r1,r2)
            while r2<len(nums) and len(d2)<(k+1):
                r2+=1
                print(r2)
                if r2<len(nums):
                    d2[nums[r2]]=d2.get(nums[r2],0)+1
            while r1<len(nums) and totalnum<k:
                r1+=1
                if r1<len(nums):
                    d1[nums[r1]]=d1.get(nums[r1],0)+1
                    if d1[nums[r1]]==m:
                        totalnum+=1
            if r1<r2:
                totalc+=r2-r1
            d1[nums[l]]-=1
            d2[nums[l]]-=1
            if d2[nums[l]]==0:
                del d2[nums[l]]
            if d1[nums[l]]==m-1:
                totalnum-=1
            if d1[nums[l]]==0:
                del d1[nums[l]]
            #print(l,r1,r2)
            #print(totalc)
        return totalc

                


            