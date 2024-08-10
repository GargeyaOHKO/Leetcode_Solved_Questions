class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        print(citations)
        c=0
        for i in citations:
            if i>c:
                c+=1
            else:
                break
        return c