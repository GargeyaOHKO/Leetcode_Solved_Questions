class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        f1,f2,f3=False,False,False
        for i in range(len(triplets)):
            if not f1 and triplets[i][0]==target[0] and triplets[i][1]<=target[1] and triplets[i][2]<=target[2]:
                f1=True
            if not f2 and triplets[i][0]<=target[0] and triplets[i][1]==target[1] and triplets[i][2]<=target[2]:
                f2=True
            if not f3 and triplets[i][0]<=target[0] and triplets[i][1]<=target[1] and triplets[i][2]==target[2]:
                f3=True
        if f1 and f2 and f3:
            return True
        else:
            return False

        