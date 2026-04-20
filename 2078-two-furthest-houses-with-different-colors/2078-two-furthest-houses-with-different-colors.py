class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxi=-1
        for i in range(len(colors)):
            if colors[i]!=colors[0]:
                maxi=max(maxi,abs(i-0))
            if colors[i]!=colors[len(colors)-1]:
                maxi=max(maxi,abs(len(colors)-1-i))
        return maxi