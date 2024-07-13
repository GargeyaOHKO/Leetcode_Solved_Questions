class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        d={}
        op=positions[:]
        for i in range(len(positions)):
            d[positions[i]]=[healths[i],directions[i]]
        directions=""
        d={k:d[k] for k in sorted(d)}
        j=0
        for i in d:
            positions[j]=i
            healths[j]=d[i][0]
            directions+=d[i][1]
            j+=1
        print(d)
        stack=[]
        for i in range(len(positions)):
            stack.append([positions[i],healths[i],directions[i]])
            while len(stack)>=2 and stack[-2][2]=="R" and stack[-1][2]=="L":
                if stack[-2][1]==stack[-1][1]:
                    stack.pop()
                    stack.pop()
                elif stack[-2][1]>stack[-1][1]:
                    stack[-2][1]-=1
                    stack.pop()
                elif stack[-2][1]<stack[-1][1]:
                    stack[-1][1]-=1
                    stack.pop(-2)
        print(stack)
        d={}
        for i in range(len(stack)):
            d[stack[i][0]]=[stack[i][1],stack[i][2]]
        l=[]
        for i in op:
            if i in d:
                l.append(d[i][0])
        return l

        