class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        hand.sort()
        dictt= {}
        for x in range(len(hand)):
            if (hand[x] not in dictt):
                dictt[hand[x]] = 1
            else:
                dictt[hand[x]] = dictt[hand[x]]+1
        chiavi = sorted(dictt.keys())
        for x in chiavi:
            while dictt[x] > 0:
                y = x
                while y < x + groupSize:
                    if dictt.get(y, 0) == 0:
                        return False
                    dictt[y] = dictt[y] - 1
                    y = y + 1
        return True