class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n1,n2=-1,-1
        for i in nums:
            if i>=n1:
                n2=n1
                n1=i
            elif i>n2:
                n2=i
        return (n1-1)*(n2-1)