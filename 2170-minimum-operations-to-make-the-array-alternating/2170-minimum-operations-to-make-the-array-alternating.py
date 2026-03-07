class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        p1,p0=1,0
        d1,d0={},{}
        for i in range(len(nums)):
            if p1<len(nums):
                d1[nums[p1]]=d1.get(nums[p1],0)+1
            if p0<len(nums):
                d0[nums[p0]]=d0.get(nums[p0],0)+1
            p1+=2
            p0+=2
        d0=dict(sorted(d0.items(),key=lambda x:x[1],reverse=True))
        d1=dict(sorted(d1.items(),key=lambda x:x[1],reverse=True))
        #print(d0)
        #print(d1)
        l0,l1=[],[]
        for i in d0:
            l0.append(i)
            if len(l0)==2:
                break
        for i in d1:
            l1.append(i)
            if len(l1)==2:
                break
        l0.append(-1)
        l1.append(-1)
        #print(l0,l1)
        mc=float('inf')
        for x in range(len(l0)):
            for z in range(len(l1)):
                m0,m1=l0[x],l1[z]
                if m1!=m0:
                    c=0
                    for i in range(len(nums)):
                        if i%2==0:
                            if nums[i]!=m0:
                                c+=1
                        else:
                            if nums[i]!=m1:
                                c+=1
                    mc=min(mc,c)
        return mc

