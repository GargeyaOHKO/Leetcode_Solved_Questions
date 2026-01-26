class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        m=float('inf')
        for i in range(len(arr)-1):
            m=min(m,abs(arr[i+1]-arr[i]))
        l=[]
        for i in range(len(arr)-1):
            if abs(arr[i+1]-arr[i])==m:
                l.append([arr[i],arr[i+1]])
        return l