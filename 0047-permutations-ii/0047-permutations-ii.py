class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(l):
            if len(l) == len(nums):
                res.append(list(nums[i] for i in l))
                return None
            for i in range(len(nums)):
                if i not in l:
                    l.append(i)
                    backtrack(l)
                    l.pop()

        backtrack([])
        s=set()
        fl=[]
        for i in res:
            if "".join(str(i)) not in s:
                fl.append(i)
                s.add("".join(str(i)))
        return fl