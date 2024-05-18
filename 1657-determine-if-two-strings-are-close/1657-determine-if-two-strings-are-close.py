class Solution(object):
    def closeStrings(self, word1, word2):
        d1={}
        d2={}
        l1,l2=[],[]
        c=0
        for i in word1:
            d1[i]=d1.get(i,0)+1
        for i in word2:
            d2[i]=d2.get(i,0)+1    
        for i in d1:
            if i in d2:  
                c+=1
                l1.append(d1[i])
                l2.append(d2[i])
        l1.sort()
        l2.sort()  
        #print(l1,l2)
        if l1==l2 and c==len(d1) and c==len(d2):
            return True       
        else:
            return False    
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        