class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx=float('-inf')
        prefgcd=[]
        for i in range(len(nums)):
            mx=max(mx,nums[i])
            prefgcd.append(math.gcd(nums[i],mx))
        prefgcd.sort()
        print()
        s=0
        for i in range(len(nums)//2):
            s+=math.gcd(prefgcd[i],prefgcd[-1-i])
        return s