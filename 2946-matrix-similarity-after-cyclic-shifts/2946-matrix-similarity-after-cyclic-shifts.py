class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for i in range(len(mat)):
            t=mat[i][:]
            for j in range(k):
                if i%2==0:
                    t=t[1:]+t[:1]
                else:
                    t=t[-1:]+t[:-1]
            if t!=mat[i]:
                return False
        return True