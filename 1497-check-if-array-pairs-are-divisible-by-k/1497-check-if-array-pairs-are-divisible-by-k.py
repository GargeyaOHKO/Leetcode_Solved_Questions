class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d={}
        for i in arr:
            d[i%k]=d.get(i%k,0)+1
        for i in d:
            dif=(k-i)%k
            if dif==i:
                if d[dif]%2!=0:
                    return False
            if dif not in d:
                return False
            elif d[i]>d[dif]:
                return False
            else:
                d[dif]-=d[i]
        return True
                


