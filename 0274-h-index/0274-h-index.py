class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        c=0
        count=1
        for i in range(len(citations)-1,-1,-1):
            if count<=citations[i]: 
                c+=1
            count+=1
        return c
        """
        :type citations: List[int]
        :rtype: int
        """
        