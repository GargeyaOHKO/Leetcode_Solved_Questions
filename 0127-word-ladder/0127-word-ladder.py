class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList=[beginWord]+wordList
        d={}
        for i in wordList:
            for j in range(len(i)):
                pattern=i[:j]+"*"+i[j+1:]
                if pattern in d:
                    d[pattern].append(i)
                else:
                    d[pattern]=[]
                    d[pattern].append(i)
        seen=set([beginWord])
        q=deque([beginWord])
        c=1
        while q:
            #print(q)
            n=len(q)
            c+=1
            for i in range(n):
                a=q.popleft()
                for j in range(len(a)):
                    pattern=a[:j]+"*"+a[j+1:]
                    for word in d[pattern]:
                        if word not in seen:
                            q.append(word)
                            seen.add(word)
                        if word==endWord:
                            return c
        


