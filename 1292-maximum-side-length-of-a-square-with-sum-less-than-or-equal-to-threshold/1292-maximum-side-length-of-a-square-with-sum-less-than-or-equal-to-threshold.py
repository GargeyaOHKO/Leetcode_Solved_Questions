class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n,m=len(mat),len(mat[0])
        maxlen=min(len(mat),len(mat[0]))
        psum=[]
        for i in range(n):
            l=[0]
            sum=0
            for j in range(m):
                sum+=mat[i][j]
                l.append(sum)
            psum.append(l)

        maxans=0
        #print(n,m)
        #print(maxlen)
        l,r=1,maxlen+1
        while l<r:
            mid=(l+r)//2
            i=mid
            flag=False
            #print("i",i)
            for j in range(m-i+1):
                s=0
                for k in range(i):
                    #print(" ",psum[k][j+i],psum[k][j])
                    s+=(psum[k][j+i]-psum[k][j])
                #print(s)
                if s<=threshold:
                    maxans=max(maxans,i)
                    l=mid+1
                    flag=True
                    break
            if flag==False:
                r=mid
        return maxans

        