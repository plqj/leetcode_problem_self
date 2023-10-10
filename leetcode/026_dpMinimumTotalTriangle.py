# 给定一个三角形 triangle ，找出自顶向下的最小路径和。
#
# 每一步只能移动到下一行中相邻的结点上。
#
# 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
# 也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
#    2
#   3 4
#  6 5 7
# 4 1 8 3

# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。


def dpMinimumTotalTriangle(triangle:list[list[str]]) -> int:
    n=len(triangle)

    # 初始化dp表
    dp=[]
    for i in range(n):
        dp.append([0]*(i+1))

    # 初始化最顶层元素
    dp[0][0]=triangle[0][0]

    # 初始化边界
    for i in range(1,n):
        dp[i][0]=triangle[i][0]+dp[i-1][0]
        dp[i][i]=triangle[i][i]+dp[i-1][i-1]

    # 动态规划核心
    for i in range(2,n):
        for j in range(1,i):
            dp[i][j]=triangle[i][j]+min(dp[i-1][j-1],dp[i-1][j])

    return min(dp[-1])

if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(dpMinimumTotalTriangle(triangle))