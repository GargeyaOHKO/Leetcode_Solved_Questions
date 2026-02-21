class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime=(2,3,5,7,11,13,17,19,23,29,31)
        c=0
        for i in range(left,right+1):
            b=bin(i)[2:]
            d=Counter(b)
            if d['1'] in prime:
                c+=1
        return c