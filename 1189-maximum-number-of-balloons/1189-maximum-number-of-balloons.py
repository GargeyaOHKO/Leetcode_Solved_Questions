class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d={"b":0,"a":0,"l":0,"o":0,"n":0}
        for i in text:
            if i=="b" or i=="a" or i=="l" or i=="o" or i=="n":
                d[i]=d.get(i,0)+1
        d["l"]=d["l"]//2
        d["o"]=d["o"]//2
        mini=float('inf')
        for i in d:
            mini=min(mini,d[i])
        return mini