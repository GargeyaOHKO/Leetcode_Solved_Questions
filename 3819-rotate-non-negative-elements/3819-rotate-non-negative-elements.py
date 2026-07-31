class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        l=[]
        for i in nums:
            if i>=0:
                l.append(i)
        if l==[]:
            return nums
        k=k%len(l)
        j=0
        for i in range(k,k+len(l)):
            n=l[i%len(l)]
            while nums[j]<0:
                j+=1
            if nums[j]>=0:
                nums[j]=n
                j+=1
        return nums
            
