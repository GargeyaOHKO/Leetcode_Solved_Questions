class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod=10**9+7
        nsmall=[len(arr)]*len(arr)
        stack=[]
        for i in range(len(arr)):
            while len(stack)>=1 and stack[-1][0]>arr[i]:
                val,index=stack.pop()
                nsmall[index]=i
            if len(stack)==0:
                stack.append([arr[i],i])
            elif stack and stack[-1][0]<=arr[i]:
                stack.append([arr[i],i])
        #print(nsmall)
        psmall=[0]*len(arr)
        stack=[]
        for i in range(len(arr)):
            #print(stack)
            #print(psmall)
            while stack and stack[-1][0]>arr[i]:
                val,index=stack.pop()
            if len(stack)==0:
                stack.append([arr[i],i])
            elif stack[-1][0]<=arr[i]:
                psmall[i]=stack[-1][1]+1
                stack.append([arr[i],i])
        #print(psmall)
        ans=0
        '''for i in range(len(arr)):
            #print("l",(i+1-psmall[i]),"r",(nsmall[i]-i),arr[i])
            ans+=(arr[i]*(nsmall[i]-i)*(i+1-psmall[i]))%mod
            #print(ans)'''
        stack=[]
        for i in range(len(arr)):
            #print(stack)
            #print(ans)
            while stack and arr[i]<stack[-1][0]:
                stack.pop()
            #print(stack)
            if len(stack)==0:
                ans+=((i+1)*(nsmall[i]-i)*arr[i])%mod
                stack.append([arr[i],i])
            elif stack[-1][0]>arr[i]:
                #print(nsmall[i]-i,i-stack[-1][1]+1)
                ans+=((nsmall[i]-i)*(i-stack[-1][1]+1)*arr[i])%mod
                stack.append([arr[i],i])
            else:
                ans+=((nsmall[i]-i)*(i-stack[-1][1])*arr[i])%mod
                stack.append([arr[i],i])
        return ans%mod
            

            