class Solution:
    def getLength(self, nums: List[int]) -> int:
        maxi=float('-inf')
        for i in range(len(nums)):
            d={}
            freq=defaultdict(int)
            for j in range(i,len(nums)):
                old=d.get(nums[j],0)
                if old>0:
                    freq[old]-=1
                    if freq[old]==0:
                        del freq[old]
                d[nums[j]]=d.get(nums[j],0)+1
                freq[d[nums[j]]]+=1
                if len(freq)==1:
                    for i in freq:
                        if freq[i]==1:
                            maxi=max(maxi,i*freq[i])
                elif len(freq)==2:
                    v1,v2=-1,-1
                    for i in freq:
                        if v1==-1:
                            v1=i
                        else:
                            v2=i
                    if v1>v2 and v1==v2*2:
                        maxi=max(maxi,v1*freq[v1]+v2*freq[v2])
                    if v2>v1 and v2==v1*2:
                        maxi=max(maxi,v1*freq[v1]+v2*freq[v2])
        return maxi