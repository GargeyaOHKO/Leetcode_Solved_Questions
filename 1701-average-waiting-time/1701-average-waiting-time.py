class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        nums=customers[:]
        l=[]
        cur=nums[0][0]+nums[0][1]
        l.append(cur-nums[0][0])
        for i in range(1,len(nums)):
            extra=cur-nums[i][0]
            #print(extra)
            if extra<0:
                extra=0
                cur=nums[i][0]+nums[i][1]
            else:
                cur+=nums[i][1] 
            l.append(extra+nums[i][1])
            #print(extra,cur,l)
        return float(sum(l)/len(nums))