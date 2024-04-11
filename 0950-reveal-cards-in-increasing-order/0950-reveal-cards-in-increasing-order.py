class Solution(object):
    def deckRevealedIncreasing(self, deck):
        deck.sort()
        l=[-1]*len(deck)
        que=deque(range(len(deck)))
        for i in deck:
            l[que.popleft()]=i
            if que:
                que.append(que.popleft())
        return l        
        
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        