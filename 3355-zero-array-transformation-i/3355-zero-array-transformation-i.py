class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        l=[0]*(len(nums)+1)
        for i in queries:
            l[i[0]]+=1
            l[i[1]+1]-=1
        newl=[]
        s=0
        for i in l:
            s+=i
            newl.append(s)
        #print(newl)
        for i in range(len(nums)):
            #print(nums[i],newl[i])
            if nums[i]>newl[i]:
                return False
        return True