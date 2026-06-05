class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        c=0
        for i in range(num1, num2+1):
            s=str(i)
            for j in range(1,len(s)-1):
                if int(s[j])>int(s[j-1]) and int(s[j])>int(s[j+1]):
                    c+=1
                if int(s[j])<int(s[j-1]) and int(s[j])<int(s[j+1]):
                    c+=1
        return c
            