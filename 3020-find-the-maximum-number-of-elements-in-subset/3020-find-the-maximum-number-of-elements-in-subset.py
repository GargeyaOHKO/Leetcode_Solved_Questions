class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        maxi=float("-inf")
        d=Counter(nums)
        if 1 in d:
            if d[1]%2==0:
                maxi=d[1]-1
            else:
                maxi=d[1]
        del d[1]
        for i in d:
            c=0
            flag=False
            #print("i",i)
            j=1
            while j<=32:
                if i**j in d and d[i**j]>1:
                    c+=2
                elif i**j in d and d[i**j]==1:
                    c+=1
                    maxi=max(maxi,c)
                    flag=True
                    break
                elif i**j not in d:
                    if c%2==1:
                        c-=1
                        maxi=max(maxi,c)
                        flag=True
                    break
                j*=2
                #print(i**j,c)
            if not flag:
                maxi=max(maxi,c-1)
        return maxi