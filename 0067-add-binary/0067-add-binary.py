class Solution:
    def addBinary(self, a: str, b: str) -> str:
        power=len(a)-1
        num1=0
        for i in range(len(a)):
            if a[i]=="1":
                num1+=2**power
            power-=1
        power=len(b)-1
        num2=0
        for i in range(len(b)):
            if b[i]=="1":
                num2+=2**power
            power-=1
        temp=num1+num2
        return bin(temp)[2:]
        '''newstr=""
        flag=False
        for i in range(20,-1,-1):
            if 2**i<=temp and not flag:
                newstr+="1"
                temp-=2**i
                flag=True
            elif 2**i<=temp and flag:
                newstr+="1"
                temp-=2**i
            elif 2**i>temp and flag:
                newstr+="0"
        if newstr=="":
            return "0"
        return newstr'''
