class Solution(object):
    def trap(self, height):
        lh=[0]*(len(height))
        rh=[0]*(len(height))
        mlh=0
        mrh=0
        c=0
        for i in range(len(height)):
            lh[i]=mlh
            rh[-i-1]=mrh
            if height[i]>mlh:
                mlh=height[i]
            if height[-i-1]>mrh:
                mrh=height[-i-1]      
        for i in range(len(height)):
            water=(min(lh[i],rh[i]))-height[i]
            if water>0:
                c+=water
        return c           
        
        """
        :type height: List[int]
        :rtype: int
        """
        