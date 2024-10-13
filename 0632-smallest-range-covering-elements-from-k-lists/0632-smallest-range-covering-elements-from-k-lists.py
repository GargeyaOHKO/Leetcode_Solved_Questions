class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        diff=float('inf')
        a,b=-1,-1
        k=len(nums)
        arr=[]
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                arr.append([nums[i][j],i])
        arr.sort(reverse=True)
        #print(arr)
        l,r=0,0
        d={}
        for r in range(len(arr)):
            if arr[r][1] not in d:
                d[arr[r][1]]=1
            else:
                d[arr[r][1]]+=1
            #print(d)
            while len(d)==k:
                if (arr[l][0]-arr[r][0])<=diff:
                    a,b=arr[l][0],arr[r][0]
                    diff=a-b
                    #print(a,b)
                d[arr[l][1]]-=1
                if d[arr[l][1]]==0:
                    del d[arr[l][1]]
                l+=1
                #print(d)
        return [b,a]
