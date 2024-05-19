class Solution(object):
    def compress(self, chars):
        c=1
        s=""
        for i in range(len(chars)):
            if i!=len(chars)-1 and chars[i]==chars[i+1]:
                c+=1
            else:
                s+=chars[i]
                if c>1:
                    s+=str(c)
                c=1    
        print(s)            
        chars[:]=[]
        for i in s:
            chars.append(i)
        return len(chars)    
        """
        :type chars: List[str]
        :rtype: int
        """
        