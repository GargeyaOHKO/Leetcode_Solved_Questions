class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        nsmall=[len(arr)]*len(arr)
        stack=[]
        m=max(arr)
        for i in range(len(arr)):
            #print(stack)
            #print(nsmall)
            while len(stack)>=1 and stack[-1][0]>arr[i]:
                val,index=stack.pop()
                nsmall[index]=i
            if len(stack)==0:
                stack.append([arr[i],i])
            elif stack and stack[-1][0]<arr[i]:
                stack.append([arr[i],i])
            elif arr[i]==m:
                stack[i]==-1
        #print(nsmall)
        ans=0
        stack=[]
        for i in range(len(arr)):
            #print(stack)
            #print(ans)
            while stack and arr[i]<stack[-1][0]:
                stack.pop()
            #print(stack)
            if len(stack)==0:
                ans+=(i+1)*(nsmall[i]-i)*arr[i]
                stack.append([arr[i],i])
            elif stack[-1][0]>arr[i]:
                #print(nsmall[i]-i,i-stack[-1][1]+1)
                ans+=(nsmall[i]-i)*(i-stack[-1][1]+1)*arr[i]
                stack.append([arr[i],i])
            else:
                ans+=(nsmall[i]-i)*(i-stack[-1][1])*arr[i]
                stack.append([arr[i],i])
        return ans
            

            