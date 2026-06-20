class Solution:
    def minLights(self, lights: list[int]) -> int:
        lit=[False]*len(lights)
        i=0
        while i<len(lights):
            if lights[i]>0:
                j=lights[i]+1
                while j>0 and i<len(lights):
                    lit[i]=True
                    
                    if i<len(lights) and lights[i]+1>=j:
                        j=lights[i]+1
                    j-=1
                    i+=1
            else:
                i+=1
                    

        i=len(lights)-1
        while i>-1:
            #print(i)
            if lights[i]>0:
                j=lights[i]+1
                while j>0 and i>-1:
                    #print(i,j)
                    lit[i]=True
                    if i>-1 and lights[i]+1>=j:
                        j=lights[i]+1
                    j-=1
                    i-=1
            else:
                i-=1
        #print(lit)
        res=[]
        c=0
        for i in lit:
            if not i:
                c+=1
            else:
                if c>0:
                    res.append(c)
                c=0
        if c>0:
            res.append(c)
        ans=0
        for i in res:
            ans+=math.ceil(i/3)
        return ans
        