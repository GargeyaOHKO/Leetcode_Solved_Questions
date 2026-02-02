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
            #print(i,dletter,total,words[i])
            if (i,total,tuple(sorted(dletter.items()))) in dp:
                return dp[(i,total,tuple(sorted(dletter.items())))]
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
            #print(tempscore,flag)
            if not flag:
                dp[(i,total,tuple(sorted(dletter.items())))]=dfs(i+1,dletter,total)
            else:
                dp[(i,total,tuple(sorted(dletter.items())))]=max(dfs(i+1,dletter,total),dfs(i+1,tempdletter,total+tempscore))
            return dp[(i,total,tuple(sorted(dletter.items())))]
        return dfs(0,dletter,0)
        