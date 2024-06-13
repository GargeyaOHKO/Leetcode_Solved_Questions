class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seatsl=[0]*102
        studentsl=[0]*102
        for i in seats:
            seatsl[i]+=1
        for i in students:
            studentsl[i]+=1
        c=0
        s=0
        i,j=1,1
        while c<len(seats):
            if seatsl[i]!=0 and studentsl[j]!=0:
                s+=abs(i-j)
                seatsl[i]-=1
                studentsl[j]-=1
                c+=1
                if seatsl[i]==0:
                    i+=1
                if studentsl[j]==0:
                    j+=1    
            if seatsl[i]==0:
                i+=1
            if studentsl[j]==0:
                j+=1
        return s        
