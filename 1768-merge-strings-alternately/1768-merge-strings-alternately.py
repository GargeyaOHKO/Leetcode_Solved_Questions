class Solution(object):
    def mergeAlternately(self, word1, word2):
        l1=0
        l2=0
        l=''
        while l1<len(word1) and l2<len(word2):
            l+=word1[l1]
            l+=word2[l2]
            l1+=1
            l2+=1
        if l1<word1:
            while l1<len(word1):
                l+=word1[l1]
                l1+=1 
        if l2<word2:
            while l2<len(word2):
                l+=word2[l2]
                l2+=1
        return l                      
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        