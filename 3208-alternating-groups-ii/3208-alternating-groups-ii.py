class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        nums=colors[:]
        n=len(nums)
        l,r=0,0
        c=0
        s=set()
        for i in range(len(nums)+k-1):
            if nums[i%n]!=nums[(i+1)%n]:
                r+=1
                if r>=k-1:
                    if i%n not in s:
                        c+=1
                        s.add(i%n)
            else:
                r=0
        return c
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        