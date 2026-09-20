class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        d=defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        c=0
        for i in d:
            if len(d[i])>2:
                f=True
                dif=d[i][1]-d[i][0]
                for j in range(len(d[i])-1):
                    if d[i][j+1]-d[i][j]!=dif:
                        f=False
                        break
                if f:
                    c+=1
        return c
