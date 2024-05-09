class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        s=0
        for i in range(len(happiness)):
            if i<k:
                if happiness[i]-i>0:
                    s+=happiness[i]-i
            else:
                break
        return s                
        