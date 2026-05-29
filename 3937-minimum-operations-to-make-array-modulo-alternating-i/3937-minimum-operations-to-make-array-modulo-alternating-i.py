class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        mini=float('inf')
        for i in range(k):
            for j in range(k):
                if i!=j:
                    c=0
                    for z in range(len(nums)):
                        if z%2==0:
                            if i<nums[z]%k:
                                c+=min(nums[z]%k-i, k-(nums[z]%k-i))
                            else:
                                c+=min(i-nums[z]%k, k-(i-nums[z]%k))
                        else:
                            if j<nums[z]%k:
                                c+=min(nums[z]%k-j, k-(nums[z]%k-j))
                            else:
                                c+=min(j-nums[z]%k, k-(j-nums[z]%k))
                    mini=min(mini,c)
        return mini
