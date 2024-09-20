class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s=sum(chalk)
        if s==k:
            return 0
        if s<k:
            k=k%s
        print(k)
        i=0
        while (k-chalk[i])>=0:
            k-=chalk[i]
            i=(i+1)%len(chalk)
        return i