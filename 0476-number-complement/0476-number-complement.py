class Solution(object):
    def findComplement(self, num):
        s=bin(num)
        #print(s)
        c=0
        n=0
        for i in range(len(s)-1,1,-1):
            #print(s[i])
            if s[i]=='0':
                n+=2**c
            c+=1
        return n

        """
        :type num: int
        :rtype: int
        """
        