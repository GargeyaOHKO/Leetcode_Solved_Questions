class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l=[]
        if len(n)==1:
            return str(int(n)-1)
        def palin(pref,isEven):
            s=str(pref)
            if not isEven:
                return int(s+s[-2::-1])
            else:
                return int(s+s[::-1])
        num=int(n)
        pref=int(n[:(len(n)+1)//2])
        l.append(palin(pref-1,len(n)%2==0))
        l.append(palin(pref,len(n)%2==0))
        l.append(palin(pref+1,len(n)%2==0))

        l.append(int("0"+'9'*(len(n)-1)))
        print(l)

        l.append(int('1'+('0'*(len(n)-1))+'1'))
        print(l)

        if str(int(n)-11)[:]==str(int(n)-11)[::-1]:
            l.append(int(n)-11)
        print(l)
        for i in range(len(l)-1,-1,-1):
            if l[i]==num:
                l.remove(num)

        fl=[]
        mindif=float('inf')
        for i in range(len(l)):
            if mindif>abs(int(n)-int(l[i])):
                mindif=abs(int(n)-int(l[i]))
                fl=[l[i]]
            if mindif==abs(int(n)-int(l[i])):
                fl.append(l[i])
        print(fl)
        return str(min(fl))
        