class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d=Counter(answers)
        ans=0
        if 0 in d:
            ans+=d[0]
            del d[0]
        for i in d:
            ans+=math.ceil((d[i])/(i+1))*(i+1)
        return ans
