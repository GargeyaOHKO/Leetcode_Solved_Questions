class Solution(object):
    def plusOne(self, digits):
        i=len(digits)-1
        carry=0
        if digits[-1]==9:
            while i>=0:
                if i==len(digits)-1 and (digits[i]+carry+1)>9:
                    carry=1
                    digits[i]=0
                elif digits[i]+carry>9:
                    digits[i]=0
                    carry=1
                else:
                    digits[i]+=1
                    return digits
                i-=1    
        if carry==1:
            digits=[1]+digits
            return digits               

        else:
            digits[-1]+=1        
        return digits
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        