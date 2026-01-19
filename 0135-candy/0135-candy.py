class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings)==1:
            return 1
        left=[1]
        right=[1]
        curr=1
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                curr+=1
                left.append(curr)
            else:
                curr=1
                left.append(curr)
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                curr+=1
                right.append(curr)
            else:
                curr=1
                right.append(curr)
        total=0
        for i in range(len(right)):
            if left[i]>right[0-i-1]:
                total+=left[i]
            else:
                total+=right[0-i-1]
        return total

        