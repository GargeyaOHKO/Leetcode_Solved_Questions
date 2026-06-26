class Solution:
    from sortedcontainers import SortedList
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                nums[i]=1
            else:
                nums[i]=-1
        pref=[0]
        c=0
        for i in nums:
            c+=i
            pref.append(c)
        mini=min(pref)
        for i in range(len(pref)):
            pref[i]=pref[i]-mini+1
        maxi=max(pref)
        sl=SortedList()
        res=0
        for i in range(len(pref)):
            sl.add(pref[i])
            res+=sl.bisect_left(pref[i])
        return res

