class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        res = 0
        for stone in stones:
            for jewel in jewels:
                if jewel == stone:
                    res += 1
        return res
        