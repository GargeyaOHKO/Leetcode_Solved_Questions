class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dfs(i,j):
            if i==len(word1) or j==len(word2):
                if i==len(word1) and j<len(word2):
                    return len(word2)-j
                if j==len(word2) and i<len(word1):
                    return len(word1)-i
                return 0
            if word1[i]==word2[j]:
                return dfs(i+1,j+1)
            else:
                return min([1+dfs(i+1,j+1),1+dfs(i+1,j),1+dfs(i,j+1)])
        return dfs(0,0)