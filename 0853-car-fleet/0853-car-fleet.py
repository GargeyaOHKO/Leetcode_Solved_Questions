class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d={}
        for i in range(len(position)):
            d[position[i]]=speed[i]
        d={k:d[k] for k in sorted(d)}
        index=0
        for i in d:
            position[index]=i
            speed[index]=d[i]
            index+=1
        stack=[]
        for i in range(len(position)):
            #print((target-position[i])/speed[i])
            time=(target-position[i])/speed[i]
            while stack and time>=stack[-1]:
                stack.pop()
            if not stack or time<stack[-1]:
                stack.append(time)
        return len(stack)