class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        one=1
        res=0
        while one<=2**31:    
            bit=n&one
            one=one<<1
            if bit>0:
                res=res|1
            else:
                res=res|0    
            if one<=2**31:
                res=res<<1
        return res    