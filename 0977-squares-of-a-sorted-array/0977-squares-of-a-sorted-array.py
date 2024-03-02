class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        mini=min(nums)
        maxi=max(nums)
        l=[0]*(max(abs(mini),abs(maxi))+1)
        lf=[]
        for i in nums:
            l[abs(i)]+=1
        for i in range(len(l)):
            if l[i]>0:
                for j in range(l[i]):
                    lf.append(i**2)                 
        return lf        
        