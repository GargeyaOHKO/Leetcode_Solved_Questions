class Solution:
    def fullJustify(self, words: List[str], mwid: int) -> List[str]:
        c=0
        l=[]
        fl=[]
        i=0
        while i<len(words):
            if c==0:
                c+=len(words[i])
                l.append(words[i])
                i+=1
            elif (c+len(words[i])+1)<=mwid:
                c+=len(words[i])+1
                l.append(words[i])
                i+=1
            else:
                s=""
                rem=mwid-c
                if len(l)==1:
                    s+=l[0]+" "*(mwid-len(l[0]))
                else:
                    each=math.ceil(rem/(len(l)-1))
                    rem=rem%(len(l)-1)
                    if rem==0:
                        rem=len(l)-1
                    for j in range(0,len(l)):
                        if j==len(l)-1:
                            s+=l[j]
                        elif rem>0:
                            s+=l[j]+(" "*(each+1))
                            rem-=1
                        else:
                            s+=l[j]+(" "*(each))
                fl.append(s)
                c=0
                l=[]
        s=" ".join(l)
        s+=" "*(mwid-len(s))
        fl.append(s)
        return fl
