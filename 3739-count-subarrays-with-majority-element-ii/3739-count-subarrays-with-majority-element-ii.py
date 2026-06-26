class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                nums[i]=1
            else:
                nums[i]=-1
        pref=[0]
        c=0
        for i in nums:
            c+=i
            pref.append(c)
        mini=min(pref)
        for i in range(len(pref)):
            pref[i]=pref[i]-mini+1
        maxi=max(pref)
        ftree=FenwickTree(maxi)
        res=0
        for i in range(len(pref)):
            res+=ftree.query(pref[i]-1)
            ftree.update(pref[i],1)
        return res

