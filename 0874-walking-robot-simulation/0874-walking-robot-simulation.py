class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        s=set((i,j) for i,j in obstacles)
        maxv=0
        dir=['N','E','S','W']
        i,j=0,0
        oper=0
        for z in commands:
            if z==-1:
                oper+=1
                oper=oper%4
            elif z==-2:
                oper-=1
                oper=oper%4
            else:
                if dir[oper]=='N':
                    for x in range(z):
                        if (i,j+1) in s:
                            break
                        j+=1
                elif dir[oper]=='E':
                    for x in range(z):
                        if (i+1,j) in s: 
                            break
                        i+=1
                elif dir[oper]=='S':
                    for x in range(z):
                        if (i,j-1) in s: 
                            break
                        j-=1
                elif dir[oper]=='W':
                    for x in range(z):
                        if (i-1,j) in s: 
                            break
                        i-=1
                maxv=max(maxv,i**2+j**2)
        return maxv