class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        if len(skills)==2:
            if skills[0]>skills[1]:
                return 0
            else:
                return 1
        d={}
        for i in range(len(skills)):
            d[skills[i]]=i    
        if k>=len(skills):
            return d[max(skills)]

        q=deque()
        for i in skills:
            q.append(i)

        c=0
        while True:
            print(q)
            num1=q.popleft()
            num2=q.popleft()
            if num1>num2:
                c+=1
                q.appendleft(num1)
                q.append(num2)
            else:
                c=1
                q.appendleft(num2)
                q.append(num1)
                if c==k:
                    return d[num2] 
            if c==k:
                return d[num1]           
                
            
            
    
            
                
        