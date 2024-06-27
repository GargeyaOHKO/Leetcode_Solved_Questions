class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minabs=float("inf")
        index=-1
        for i in range(len(arr)):
            if abs(x-arr[i])<minabs:
                minabs=abs(x-arr[i])
                index=i
        print(index)
        l,r=index,index
        k-=1
        #print(l,r)
        while k>0:
            print(l,r,k)
            if l-1>=0 and r+1<len(arr) and abs(arr[l-1]-x)<=abs(arr[r+1]-x):
                l-=1
                k-=1
            elif l-1>=0 and r+1<len(arr) and abs(arr[l-1]-x)>abs(arr[r+1]-x):
                r+=1
                k-=1
            elif l-1>=0 and r+1>=len(arr):
                l-=1
                k-=1
            elif l-1<0 and r+1<len(arr):
                r+=1
                k-=1
            print(l,r,k)
            print()
        print(l,r)
        fl=[]
        for i in range(l,r+1): 
            fl.append(arr[i])
        return fl