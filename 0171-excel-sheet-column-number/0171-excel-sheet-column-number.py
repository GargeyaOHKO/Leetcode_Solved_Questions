class Solution(object):
    def titleToNumber(self, columnTitle):
        posi=26
        count=ord(columnTitle[-1])-64
        for i in range(len(columnTitle)-2,-1,-1):
            count+=((ord(columnTitle[i])-64)*posi)
            posi*=26
        return count
        """
        :type columnTitle: str
        :rtype: int
        """
        