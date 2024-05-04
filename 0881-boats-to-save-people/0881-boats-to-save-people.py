class Solution(object):
    def numRescueBoats(self, people, limit):
        c=0
        people.sort()
        index=len(people)
        for i in range(len(people)):
            if people[i]>=limit:
                index=i
                break
        c+=len(people)-index        
        people[:]=people[:index]
        l,r=0,len(people)-1
        while len(people)!=0:
            #print(people,l,r)
            if l==r:
                people.pop(l)
                c+=1
            elif people[l]+people[r]<=limit:
                people.pop(r)
                people.pop(l)
                c+=1
                l=0
                r=len(people)-1
            else:
                r-=1
        return c
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        