class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        stack=[(float('inf'),1)]
        res=len(nums)
        for i in range(len(nums)):
            #print(stack)
            while nums[i]>stack[-1][0]:
                stack.pop()
            if nums[i]==stack[-1][0]:
                c=stack.pop()[1]
                stack.append((nums[i],c+1))
                res+=c+1
            if nums[i]<stack[-1][0]:
                stack.append((nums[i],0))
        return res

