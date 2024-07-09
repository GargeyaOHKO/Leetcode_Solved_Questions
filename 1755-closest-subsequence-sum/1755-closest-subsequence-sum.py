class Solution(object):
    def minAbsDifference(self, nums, goal):
        arr1,arr2=nums[:len(nums)//2],nums[len(nums)//2:]
        def dfs(arr,i,s,l,dp):
            if i>=len(arr):
                l.append(s)
                return None
            if (i,s) in dp:
                return dp[(i,s)]
            dp[(i,s)]=min(dfs(arr,i+1,s+arr[i],l,dp) , dfs(arr,i+1,s,l,dp))
            return l
        l1=dfs(arr1,0,0,[],{})
        l2=dfs(arr2,0,0,[],{})
        l2.sort()
        mini=float('inf')
        for i in l1:
            rem=goal-i
            index=bisect_left(l2,rem)
            if index<len(l2):
                mini=min(mini,abs(rem-l2[index]))
            if index>0:
                mini=min(mini,abs(rem-l2[index-1]))
        return mini
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        