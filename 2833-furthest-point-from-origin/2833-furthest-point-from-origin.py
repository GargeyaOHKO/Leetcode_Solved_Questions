class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        d={'L':0,'R':0,'_':0}
        for i in moves:
            d[i]=d.get(i,0)+1
        if d['L']>=d['R']:
            return (d['L']-d['R'])+d['_']
        else:
            return (d['R']-d['L'])+d['_']