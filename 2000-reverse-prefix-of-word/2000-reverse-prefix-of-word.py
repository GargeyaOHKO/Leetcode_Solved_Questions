class Solution(object):
    def reversePrefix(self, word, ch):
        index=0
        for i in range(len(word)):
            if word[i]==ch:
                index=i
                break
        l=index
        if index!=0:
            word=word[:index+1][::-1]+word[index+1:]
        return word        

        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        