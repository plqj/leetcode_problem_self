# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。

# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。


def dpMinimum(grid:list[list[int]]):
    m=len(grid)
    n=len(grid[0])
    # 用dp表来写，先初始化
    dp=[[1e6 for _ in range(n)] for _ in range(m)] # 构建m*n的dp表
    dp[0][0]=grid[0][0]
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                continue
            elif i==0 and j!=0:
                dp[i][j]=dp[i][j-1]+grid[i][j]
            elif j==0 and i!=0:
                dp[i][j]=dp[i-1][j]+grid[i][j]
            else:
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
    return dp[-1][-1]


def dpMinimum_memoryfree(grid:list[list[int]]):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i==0 and j==0:continue
            elif i==0 and j!=0:grid[i][j]=grid[i][j-1]+grid[i][j]
            elif j==0 and i!=0:grid[i][j]=grid[i-1][j]+grid[i][j]
            else:grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j]
    return grid[-1][-1]


if __name__ == '__main__':
    grid=[[1,2,3],[4,5,6]]
    print(dpMinimum(grid))
    print(dpMinimum_memoryfree(grid))