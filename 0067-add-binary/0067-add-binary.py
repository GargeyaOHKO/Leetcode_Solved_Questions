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
        newstr=""
        while temp>0:
            newstr=str(temp%2)+newstr
            temp=temp//2
        if newstr=="":
            return '0'
        return newstr