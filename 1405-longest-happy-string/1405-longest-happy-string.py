class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h=[]
        l=[]
        if a>0:
            heapq.heappush(h,(-a,"a"))
        if b>0:
            heapq.heappush(h,(-b,"b"))
        if c>0:
            heapq.heappush(h,(-c,"c"))
        s=""
        while(h):
            #print(h)
            num,char=heapq.heappop(h)
            if len(s)>1 and s[-1]==s[-2]==char:
                l.append((num,char))
                if not h:
                    break
                else:
                    num,char=heapq.heappop(h)
                    n,c=l.pop()
                    heapq.heappush(h,(n,c))
                    s+=char
                    num+=1
                    if num<0:
                        heapq.heappush(h,(num,char))               
            else:
                #print("else")
                s+=char
                num+=1
                if num<0:
                    heapq.heappush(h,(num,char))
            heapq.heapify(h)
            #print(s)
            #print(h)
        return s