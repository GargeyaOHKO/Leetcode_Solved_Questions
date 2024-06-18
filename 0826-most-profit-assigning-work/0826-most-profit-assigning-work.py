class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        l=[]
        c=0
        for i in range(len(difficulty)):
            l.append([difficulty[i],profit[i]])
        l.sort()
        worker.sort()
        i,j=0,0
        #print(l)
        #print(worker)
        while j<len(worker) and i<len(worker):
            #print(l[i][0],worker[j])
            #print(c)
            #print(i,j)
            if i==len(l)-1 and l[i][0]<=worker[j]:
                c+=l[i][1]
                j+=1
            elif i<len(l)-1 and l[i][0]<=worker[j] and l[i+1][0]>worker[j]:
                c+=l[i][1]
                j+=1
            elif i<len(l)-1 and (l[i][0]>worker[j] or (l[i][0]<=worker[j] and l[i+1][0]<=worker[j])):
                i+=1
            elif i==len(l)-1 and l[i][0]<=worker[j]:
                c+=l[i][1]
                j+=1
            else:
                j+=1
        return c

        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        