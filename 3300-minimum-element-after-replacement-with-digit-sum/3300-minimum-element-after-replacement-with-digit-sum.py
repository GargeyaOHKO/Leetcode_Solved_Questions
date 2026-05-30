class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini=float('inf')
        for i in nums:
            s=str(i)
            c=0
            for j in s:
                c+=int(j)
            mini=min(mini,c)
        return mini
