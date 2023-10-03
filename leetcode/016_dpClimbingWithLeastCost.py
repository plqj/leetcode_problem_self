# 给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。
# 一旦你支付此费用，即可选择向上爬一个或者两个台阶。
#
# 你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
#
# 请你计算并返回达到楼梯顶部的最低花费。


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        prev = curr = 0
        for i in range(2, n + 1):
            nxt = min(curr + cost[i - 1], prev + cost[i - 2])
            prev, curr = curr, nxt
        return curr

if __name__ == '__main__':
    cost=[10,15,20]
    test=Solution()
    print(test.minCostClimbingStairs(cost))