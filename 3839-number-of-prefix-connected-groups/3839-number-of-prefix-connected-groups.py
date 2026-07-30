class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        d=defaultdict(int)
        for i in words:
            if len(i)>=k:
                d[i[:k]]+=1
        
        c=0
        for i in d:
            if d[i]>1:
                c+=1
        return c