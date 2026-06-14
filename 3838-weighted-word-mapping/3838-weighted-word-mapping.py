class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        s=""
        for i in words:
            c=0
            for j in range(len(i)):
                c+=weights[ord(i[j])-97]
            s+=chr(96+(26-(c%26)))
        return s
