class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        lis=[]
        for i in range(len(arr)-1):
            l=i
            r=len(arr)-1
            while r>l:
                lis.append([float(arr[l]/arr[r]),arr[l],arr[r]])
                r-=1
        lis.sort()       
        return [lis[k-1][1],lis[k-1][2]]