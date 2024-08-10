class Solution:
    def hIndex(self, citations: List[int]) -> int:
        avg=math.ceil(len(citations)/2)
        c=0
        for i in citations:
            if i>=avg:
                c+=1
        return c