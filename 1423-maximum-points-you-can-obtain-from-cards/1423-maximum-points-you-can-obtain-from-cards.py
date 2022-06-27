class Solution:
    def maxScore(self, cards: List[int], k: int) -> int:
        l, r = 0, len(cards)-k
        total = sum(cards[r:])
        res = total
        while r < len(cards):
            total += cards[l] - cards[r]
            res = max(res, total)
            l += 1
            r += 1
        return res