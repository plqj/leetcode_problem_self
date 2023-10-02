# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
import time


# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。


class Selling_Stock(object):
    def __init__(self,prices:list):
        self.prices=prices
        self.price_iter=reversed(prices) # reversed iterator
        self.n=len(prices)

    def count(self):
        out=0
        for i in range(self.n):
            item=self.price_iter.__next__() # 当前元素
            out_temp=max(self.prices[i:]) - item
            if out_temp<=0:
                continue

            if out_temp>out:
                out=out_temp
                del out_temp
        return out

    def maxProfit(self):
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in self.prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit


if __name__ == '__main__':
    p=[7,1,5,3,6,4,3,5,2,12,3,4,1,4,6,3,6,13,3,6,8,3,5,3,1,8,6,7,3,432,1,3]
    test=Selling_Stock(p)
    t1=time.time()
    print(test.count())
    t2=time.time()
    print(t2-t1)

    t1=time.time()
    print(test.maxProfit())
    t2=time.time()
    print(t2-t1)