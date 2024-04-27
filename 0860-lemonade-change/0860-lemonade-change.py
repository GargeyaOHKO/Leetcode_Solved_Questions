class Solution(object):
    def lemonadeChange(self, bills):
        d={5:0,10:0,20:0}
        if bills[0]==10 or bills[0]==20:
            return False
        for i in bills:
            d[i]+=1 
            if i==10:
                d[5]-=1
                if d[5]<0:
                    return False
            elif i==20:
                if d[10]>0:
                    d[10]-=1
                    d[5]-=1
                elif d[10]<=0:
                    d[5]-=3
                if d[5]<0:
                    return False      
            print(d)         
        return True                  
        """
        :type bills: List[int]
        :rtype: bool
        """
        