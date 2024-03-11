class Solution(object):
    def customSortString(self, order, s):
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        s=""        
        for i in order:
            if i in d and d[i]>0:
                while d[i]>0:
                    s=s+i
                    d[i]-=1
        for i in d:
            while d[i]>0: 
                s=s+i    
                d[i]-=1    
        return s         

        """
        :type order: str
        :type s: str
        :rtype: str
        """
        