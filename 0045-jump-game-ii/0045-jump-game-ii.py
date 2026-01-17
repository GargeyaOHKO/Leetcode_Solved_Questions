class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        prev=0
        i=nums[0]
        maxi=0
        jump=0
        while i<(len(nums)-1):
            #print(i,maxi,prev)
            tempi=i
            while i>prev:
                #print(i,prev)
                maxi=max(maxi,i+nums[i])    
                #print("maxi",maxi)        
                i-=1
            prev=tempi
            i=maxi
            jump+=1
        return jump+1



        