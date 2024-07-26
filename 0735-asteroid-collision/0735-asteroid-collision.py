class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[asteroids[0]]
        for i in range(1,len(asteroids)):
            stack.append(asteroids[i])
            print(stack)
            while len(stack)>=2 and stack[-2]>0 and stack[-1]<0:
                if abs(stack[-2])==abs(stack[-1]):
                    stack.pop()
                    stack.pop()
                elif abs(stack[-2])<abs(stack[-1]):
                    stack.pop(-2)  
                elif abs(stack[-2])>abs(stack[-1]):
                    stack.pop(-1) 
  
        return stack