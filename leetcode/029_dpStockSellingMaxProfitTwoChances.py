# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 输入：prices = [3,3,5,0,0,3,1,4]
# 输出：6
# 解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。


def dpStockSellingMaxProfitTwoChances(prices:list[int]) -> int:
    n = len(prices)
    prices.append(0)  # 结尾处加一个零保证列表长度足够
    profit = 0  # 初始化利润
    is_hold = 0  # 是否有股票
    earned=[]

    for i in range(n):
        if is_hold == 0:  # 当前不持有股票，那就买
            profit -= prices[i]
            is_hold = 1

        # 考虑当天是否要卖出去
        if prices[i] > prices[i + 1]:  # 赶紧卖掉当天的，不然就亏了
            profit += prices[i]
            is_hold = 0
            earned.append(profit)
            profit=0

    if len(earned)==1:return earned[0]
    else: return sorted(earned,reverse=True)[0]+sorted(earned,reverse=True)[1]


def maxProfit(prices: list[int]) -> int:
    n = len(prices)
    dp = [[0, 0, 0, 0] for _ in range(n)]
    dp[0] = [-prices[0], 0, -prices[0], 0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], -prices[i])
        dp[i][1] = max(dp[i - 1][1], + prices[i] + dp[i - 1][0])
        dp[i][2] = max(dp[i - 1][2], - prices[i] + dp[i - 1][1])
        dp[i][3] = max(dp[i - 1][3], + prices[i] + dp[i - 1][2])
    return dp[-1][-1]


if __name__ == '__main__':
    prices=[4,4,4]
    print(dpStockSellingMaxProfitTwoChances(prices))
    print(maxProfit(prices))

    # 第一个方法本质是基于贪心算法的，不一定能拿到全局最优解，第二个方法基于动态规划。