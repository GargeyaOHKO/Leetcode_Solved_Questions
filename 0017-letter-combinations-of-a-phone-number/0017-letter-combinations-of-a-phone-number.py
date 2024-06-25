class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[]
        def dfs(i,s):
            if i>=len(digits):
                res.append(s)
                return None
            for j in d[str(digits[i])]:
                s+=j
                dfs(i+1,s)
                s=s[:-1]
            return res
        return dfs(0,"")