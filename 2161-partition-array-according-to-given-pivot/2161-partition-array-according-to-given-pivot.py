class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res=[]
        same=[]
        big=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                res.append(nums[i])
            elif nums[i]==pivot:
                same.append(nums[i])
            else:
                big.append(nums[i])
        for i in same:
            res.append(i)
        for i in big:
            res.append(i)
        return res