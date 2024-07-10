class Solution(object):
    def minOperations(self, logs):
        c=0
        for i in logs:
            if len(i)>=3 and i[-3:]=='../' and c>0:
                c-=1
            if len(i)>=2 and i[-2:]=='./':
                continue
            if len(i)>=1 and i[-1:]=='/':
                c+=1
        return c
        """
        :type logs: List[str]
        :rtype: int
        """
        