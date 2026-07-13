class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res=[]
        def dfs(i):
            if low<=int(i)<=high:
                res.append(int(i))
            if len(i)>11:
                return None
            last=i[-1:]
            n=int(last)+1
            if n>9:
                return None
            dfs(i+str(n))
        for i in range(1,9):
            dfs(str(i))
        res.sort()
        return res