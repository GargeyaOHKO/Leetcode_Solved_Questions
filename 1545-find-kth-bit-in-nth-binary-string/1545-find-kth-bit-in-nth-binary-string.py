class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        for i in range(n-1):
            new="1"
            add=list(s)
            for i in range(len(add)):
                if add[i]=="0":
                    add[i]="1"
                else:
                    add[i]="0"
            add.reverse()
            s+=new+"".join(add)   
        #print(s)
        return s[k-1]  