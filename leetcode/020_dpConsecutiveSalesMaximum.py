# 某公司每日销售额记于整数数组sales，请返回所有连续一或多天销售额总和的最大值。
import math


# 要求实现时间复杂度为O(n)的算法。


# 输入：sales = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 输出：6
# 解释：[4, -1, 2, 1]
# 此连续四天的销售总额最高，为6。
#
#
# 输入：sales = [5, 4, -1, 7, 8]
# 输出：23
# 解释：[5, 4, -1, 7, 8]
# 此连续五天的销售总额最高，为23。


def dp_sales(sales:list[int]):
    n=len(sales)
    dp=[-1e-6]*(n+1)
    ans=sales[0]
    for i in range(1,n+1):
        dp[i] = max(sales[i-1], dp[i-1] + sales[i-1])
    return max(dp)


if __name__ == '__main__':
    sales = [3,-2,5, 4, -1, 7, 8,-2,9,-1,2,-4]
    print(dp_sales(sales))