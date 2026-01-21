class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        m=max(nums)
        ans=[0]*len(nums)
        stack=[]
        new=nums[:]
        for i in nums:
            new.append(i)
        #print(new)
        for i in range(len(new)):
            while len(stack)>=1 and new[i]>stack[-1][0]:
                ans[stack[-1][1]]=new[i]
                stack.pop()
            if new[i]==m and i<len(nums):
                ans[i]=-1
            else:
                if i<len(nums):
                    stack.append((new[i],i))
            #print(stack)
            #print(ans)
        #print(ans)
        return ans