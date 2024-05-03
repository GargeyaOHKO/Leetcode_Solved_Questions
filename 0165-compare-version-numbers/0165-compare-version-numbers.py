class Solution(object):
    def compareVersion(self, version1, version2):
        l1=list(version1.split("."))
        l2=list(version2.split("."))
        l=max(len(l1),len(l2))
        if len(l1)<l:
            for i in range(l-len(l1)):
                l1.append(0)
        if len(l2)<l:
            for i in range(l-len(l2)):
                l2.append(0)        

        for i in range(max(len(l1),len(l2))): 
            if int(l1[i])>int(l2[i]):
                return 1
            elif int(l1[i])<int(l2[i]): 
                return -1
        return 0        
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        