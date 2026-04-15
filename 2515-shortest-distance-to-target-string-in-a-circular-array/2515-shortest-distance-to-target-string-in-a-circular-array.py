class Solution:
    def closestTarget(self, words: List[str], target: str, start: int) -> int:
        mini=float('inf')
        for i in range(start,start+len(words),1):
            if words[i%len(words)]==target:
                mini=min(mini,i-start)
        words=words[::-1]
        for i in range(len(words)-1-start,len(words)-1-start+len(words),1):
            if words[i%len(words)]==target:
                mini=min(mini,i-(len(words)-1-start))
        if mini==float('inf'):
            return -1
        else:
            return mini
