class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        dletter={}
        for i in letters:
            if i in dletter:
                dletter[i]+=1
            else:
                dletter[i]=1
        dp={}
        def dfs(i,dletter,total):
            if i>=len(words):
                return total
            if (i,total,tuple(dletter.get(chr(i+97), 0) for i in range(26))) in dp:
                return dp[(i,total,tuple(dletter.get(chr(i+97), 0) for i in range(26)))]
            currword=Counter(words[i])
            tempscore=0
            tempdletter=copy.deepcopy(dletter)
            flag=True
            for j in currword:
                if j in dletter and currword[j]<=tempdletter[j]:
                    tempdletter[j]-=currword[j]
                    tempscore+=score[(ord(j)-97)]*currword[j]
                else:
                    flag=False
            if not flag:
                dp[(i,total,tuple(dletter.get(chr(i+97), 0) for i in range(26)))]=dfs(i+1,dletter,total)
            else:
                dp[(i,total,tuple(dletter.get(chr(i+97), 0) for i in range(26)))]=max(dfs(i+1,dletter,total),dfs(i+1,tempdletter,total+tempscore))
            return dp[(i,total,tuple(dletter.get(chr(i+97), 0) for i in range(26)))]
        return dfs(0,dletter,0)
        