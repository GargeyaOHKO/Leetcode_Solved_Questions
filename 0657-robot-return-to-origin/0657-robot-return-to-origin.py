class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ud,lr=0,0
        for i in moves:
            if i=='U':
                ud+=1
            elif i=='D':
                ud-=1
            elif i=='R':
                lr+=1
            else:
                lr-=1
        if ud==0 and lr==0:
            return True
        else:
            return False