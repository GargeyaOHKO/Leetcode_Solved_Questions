class Solution(object):
    def threeConsecutiveOdds(self, arr):
        c=0
        for i in arr:
            if i%2==1:
                c+=1
            else:
                c=0
            if c==3:
                return True
        return False
        """
        :type arr: List[int]
        :rtype: bool
        """
        