from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        sl=SortedList()
        sl.add(nums[0])
        l,r=0,0
        maxl=float("-inf")
        while r<len(nums):
            #print(q)
            diff=sl[-1]-sl[0]
            #print(diff)
            if diff>limit:
                sl.remove(nums[l])
                l+=1
            elif diff<=limit:
                maxl=max(maxl,r-l+1)
                r+=1      
                if r<len(nums):
                    sl.add(nums[r])
        return maxl

