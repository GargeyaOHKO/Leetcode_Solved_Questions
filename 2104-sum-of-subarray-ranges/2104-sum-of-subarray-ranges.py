class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        prevs=[0]*len(nums)
        nexts=[len(nums)]*len(nums)
        stack=[]
        for i in range(len(nums)):
            if stack and stack[-1][0]<nums[i]:
                prevs[i]=stack[-1][1]+1
            if not stack:
                stack.append([nums[i],i])
            elif stack[-1][0]>nums[i]:
                stack.append([nums[i],i])
        stack=[]
        for i in range(len(nums)-1,-1,-1):
            if stack and stack[-1][0]<nums[i]:
                nexts[i]=stack[-1][1]
                stack.append([nums[i],i])
            if not stack:
                stack.append([nums[i],i])
            elif stack[-1][0]>nums[i]:
                stack.append([nums[i],i])
        totals=0
        for i in range(len(nums)):
            totals+=nums[i]*(i-prevs[i]+1)*(nexts[i]-i)
        print(totals)

        nextl=[len(nums)]*len(nums)
        prevl=[0]*len(nums)
        stack=[]
        for i in range(len(nums)):
            if stack and stack[-1][0]>nums[i]:
                prevl[i]=stack[-1][1]+1
            if not stack:
                stack.append([nums[i],i])
            elif stack[-1][0]<=nums[i]:
                stack.append([nums[i],i])
        print(prevl)
        stack=[]
        for i in range(len(nums)-1,-1,-1):
            if stack and stack[-1][0]>nums[i]:
                nextl[i]=stack[-1][1]
                stack.append([nums[i],i])
            if not stack:
                stack.append([nums[i],i])
            elif stack[-1][0]<nums[i]:
                stack.append([nums[i],i])
        print(nextl)
        totall=0
        for i in range(len(nums)):
            totall+=nums[i]*(i-prevl[i]+1)*(nextl[i]-i)
            print(totall)
        print(totall)
        return totall-totals