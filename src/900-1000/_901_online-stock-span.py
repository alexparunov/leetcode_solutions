"""
https://leetcode.com/problems/online-stock-span/

"""


class StockSpanner:
    def __init__(self):
        self.stocks = []
        self.days = -1

    def next(self, price: int) -> int:
        self.days += 1

        while self.stocks and self.stocks[-1][1] <= price:
            self.stocks.pop()

        if not self.stocks:
            self.stocks.append((self.days, price))
            return self.days + 1

        res_idx = self.stocks[-1][0]
        self.stocks.append((self.days, price))
        return self.days - res_idx
