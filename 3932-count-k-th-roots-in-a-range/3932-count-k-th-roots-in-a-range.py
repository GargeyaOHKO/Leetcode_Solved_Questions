class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        if k==1:
            return r-l+1
        c=0
        for i in range(int(math.pow(r,0.5))+1):
            if l<=(i**k)<=r:
                c+=1
        return c

        