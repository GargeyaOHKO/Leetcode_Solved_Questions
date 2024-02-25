class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        one=1
        res=0
        for i in range(32):
            bit=n&1
            n=n>>1
            res=res|bit
            if i<31:
                res=res<<1
        return res    