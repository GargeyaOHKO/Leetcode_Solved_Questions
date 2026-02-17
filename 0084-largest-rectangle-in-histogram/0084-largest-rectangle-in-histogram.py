class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxarea=0
        for i in range(len(heights)):
            index=-1
            while stack and heights[i]<stack[-1][0]:
                val,index=stack.pop()
                maxarea=max(maxarea,(i-index)*val)
            if not stack or heights[i]>stack[-1][0]:
                if index!=-1:
                    stack.append([heights[i],index])
                else:
                    stack.append([heights[i],i])
        for i in range(len(stack)):
            val,index=stack.pop()
            maxarea=max(maxarea,(len(heights)-index)*val)
        return maxarea

            
            