class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize=maxSize
        self.l=[-1]*(maxSize+1)
        self.top=0

    def push(self, x: int) -> None:
        if self.top!=self.maxSize:
            self.l[self.top]=x
            self.top+=1
        print(self.l)

    def pop(self) -> int:
        if self.top>0:
            self.top-=1
            num=self.l[self.top]
            self.l[self.top]=-1
            return num
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(0,min(self.top,k)):
            self.l[i]+=val
        #return self.l[:self.top]


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)