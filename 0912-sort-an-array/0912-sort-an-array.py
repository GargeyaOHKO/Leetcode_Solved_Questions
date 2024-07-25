class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res=[]
        def merges(nums): 
            if len(nums)<=1:
                return nums
            left=nums[:len(nums)//2]
            right=nums[len(nums)//2:]
            left=merges(left)
            right=merges(right)
            return merge(left,right)
        def merge(l,r):
            p1,p2=0,0
            res=[]
            while p1<len(l) and p2<len(r):
                if l[p1]<r[p2]:
                    res.append(l[p1])
                    p1+=1
                else:
                    res.append(r[p2])
                    p2+=1
            while p1<len(l):
                res.append(l[p1])
                p1+=1
            while p2<len(r):
                res.append(r[p2])
                p2+=1
            return res
        return merges(nums)