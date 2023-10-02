# 解决N皇后问题

# 根据国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
# 给定 𝑛 个皇后和一个 𝑛 × 𝑛 大小的棋盘，寻找使得所有皇后之间无法相互攻击的摆放方案。


def backtrack(row:int,
              n:int,
              state:list[list[str]],
              res:list[list[list[str]]],
              cols:list[bool],
              diags1:list[bool],
              diags2:list[bool]):
    # backtrack 基本单元
    # 回溯算法第一步，判断是否到达终点
    if row == n:
        res.append([list(row) for row in state])
        return

    # 开始按照列来遍历并计算当前格子是否可以放置皇后
    for col in range(n):
        # 计算主副对角线index
        diag1= row-col+n-1
        diag2= row+col
        # 判断
        if not cols[col] and not diags1[diag1] and not diags2[diag2]:
            # 放置皇后
            state[row][col] = "Q"
            # 更新状态
            cols[col] = diags1[diag1] = diags2[diag2] = True

            # 放置下一行
            backtrack(row+1,n, state, res, cols, diags1, diags2)

            # 将该格子皇后位置撤销
            state[row][col] = "#"
            # 状态更新撤销为False
            cols[col] = diags1[diag1] = diags2[diag2] = False


def n_queens(n:int)-> (list[list[list[str]]],int):
    # 初始化
    state = [["#" for _ in range(n)] for _ in range(n)]

    # 记录列是否有皇后
    cols = [False] * n

    # 记录主对角线是否有皇后
    diags1 = [False] * (2 * n - 1)

    # 记录副对角线是否有皇后
    diags2 = [False] * (2 * n - 1)

    res = []

    backtrack(0, n, state, res, cols, diags1, diags2)

    return res,len(res)

print(n_queens(8))