class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxarea=0
        for i in range(len(heights)):
            #print(stack,maxarea)
            index=-1
            while stack and heights[i]<stack[-1][1]:
                index,height=stack.pop()
                maxarea=max(maxarea,height*(i-index))
            if not stack or heights[i]>stack[-1][1]:
                if index!=-1:
                    stack.append([index,heights[i]])
                else:
                    stack.append([i,heights[i]])
        #print(stack,maxarea)
        while stack:
            index,height=stack.pop()
            maxarea=max(maxarea,height*(len(heights)-index))
        return maxarea
            