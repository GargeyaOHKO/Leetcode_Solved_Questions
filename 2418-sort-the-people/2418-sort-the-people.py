class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        for i in range(len(names)):
            d[heights[i]]=names[i]
        def merge(l):
            if len(l)<=1:
                return l
            left=l[:len(l)//2]
            right=l[len(l)//2:]
            left=merge(left)
            right=merge(right)
            return mergel(left,right)
        def mergel(left,right):
            newl=[]
            p1,p2=0,0
            while p1<len(left) and p2<len(right):
                if left[p1]<right[p2]:
                    newl.append(right[p2])
                    p2+=1
                else:
                    newl.append(left[p1])
                    p1+=1
            while p1<len(left):
                newl.append(left[p1])
                p1+=1
            while p2<len(right):
                newl.append(right[p2])
                p2+=1
            return newl
        newl=merge(heights)
        res=[]
        for i in newl:
            res.append(d[i])
        return res
