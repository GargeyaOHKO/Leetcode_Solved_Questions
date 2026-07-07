class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees)<=3:
            return trees

        def dot(A,B,C):
            return (C[1]-B[1])*(B[0]-A[0])-(B[1]-A[1])*(C[0]-B[0])

        temp1=[]
        trees.sort()
        for i in trees:
            while len(temp1)>=2 and dot(temp1[-2],temp1[-1],i)<0:
                temp1.pop()
            temp1.append(i)
        temp2=[]
        for i in trees[::-1]:
            while len(temp2)>=2 and dot(temp2[-2],temp2[-1],i)<0:
                temp2.pop()
            temp2.append(i)
        s=set()
        for i in temp1:
            s.add(tuple(i))
        for i in temp2:
            s.add(tuple(i))
        return list(s)