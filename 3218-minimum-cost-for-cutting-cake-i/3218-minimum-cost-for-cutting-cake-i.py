class Solution:
    def minimumCost(self, m: int, n: int, hCut: List[int], vCut: List[int]) -> int:
        vPart=1
        hPart=1
        hCut.sort()
        vCut.sort()
        c=0
        while hCut and vCut:
            if hCut[-1]>vCut[-1]:
                c+=hCut[-1]*vPart
                hPart+=1
                hCut.pop()
            else:
                c+=vCut[-1]*hPart
                vPart+=1
                vCut.pop()
        while hCut:
            c+=hCut[-1]*vPart
            hPart+=1
            hCut.pop()
        while vCut:
            c+=vCut[-1]*hPart
            vPart+=1
            vCut.pop()
        return c

            