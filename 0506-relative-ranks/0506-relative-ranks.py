class Solution(object):
    def findRelativeRanks(self, score):
        scorecopy=[]
        scorecopy[:]=score[:]
        score.sort(reverse=True)
        l=[]
        d={}
        for i in range(len(score)):
            if i==0:
                d[score[i]]="Gold Medal"
            elif i==1:
                d[score[i]]="Silver Medal"
            elif i==2:
                d[score[i]]="Bronze Medal"
            else:
                d[score[i]]=str(i+1)
        for i in scorecopy:
            l.append(d[i])        
        return l
        """
        :type score: List[int]
        :rtype: List[str]
        """
        