class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.total=0
        def merge(nums):
            if len(nums)<=1:
                return nums
            mid=len(nums)//2
            left=merge(nums[:mid])
            right=merge(nums[mid:])
            i,j=0,0
            #print(left,right)
            for i in range(len(left)):
                while j<len(right) and left[i]>(right[j]*2):
                    j+=1
                self.total+=j
            #print(self.total)
            i,j=0,0
            newl=[]
            while i<len(left) and j<len(right):
                if left[i]>right[j]:
                    newl.append(right[j])
                    j+=1
                else:
                    newl.append(left[i])
                    i+=1
            while i<len(left):
                newl.append(left[i])
                i+=1
            while j<len(right):
                newl.append(right[j])
                j+=1
            #print(newl)
            return newl
        merge(nums)
        return self.total