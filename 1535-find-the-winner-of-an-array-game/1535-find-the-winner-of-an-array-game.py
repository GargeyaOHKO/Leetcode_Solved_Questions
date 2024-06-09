class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        q=deque()
        for i in arr:
            q.append(i)
        c=0    
        if k>len(arr):
            return max(arr)
        while True:
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
                    return num2
            if c==k:
                return num1        
        