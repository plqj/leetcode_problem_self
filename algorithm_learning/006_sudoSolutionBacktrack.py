# 编写一个程序，通过填充空格来解决数独问题。
#
# 数独的解法需 遵循如下规则：
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 数独部分空格内已填入了数字，空白格用 '.' 表示。


def is_valid(board,row,col,val):
    # 同行冲突
    for i in range(9):
        if board[row][i] == str(val):
            return False

    # 同列冲突
    for j in range(9):
        if board[j][col] == str(val):
            return False

    # 宫格冲突
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row,start_row+3):
        for j in range(start_col,start_col+3):
            if board[i][j] == str(val):
                return False

    return True


def backtrack(board:list[list[str]]):
    # 拿到一个board后马上判断是否可以输出结果
    for row in range(len(board)): # 遍历行
        for col in range(len(board[0])): # 遍历列
            if board[row][col] != ".": # 当前元素为数字，则跳过
                continue
            for i in range(1,10):
                if is_valid(board,row,col,i): # 如果可以放置
                    board[row][col]=str(i) # 将当前数字放置到对应的位置上
                    if backtrack(board=board): # 前进到下一次迭代 本题的终止条件是在这个地方引入的！！！和N皇后问题在函数一开始判断是不一样的
                        return True # 如果递归成功（找到了一个解），则返回 True，表示数独已经解决。
                    board[row][col]="." # 如果递归失败，就将当前空格重新设为 "."，表示清除之前尝试的数字，然后尝试下一个数字
            # 若数字1-9都不能成功填入空格，返回False无解
            return False # 若数字1～9都不能填，则返回False无解

    return True # 如果成功填充了所有的空格，那么整个数独问题就被解决了，返回 True 表示解决成功。


def solve(board):
    backtrack(board=board)


if __name__ == '__main__':
    map = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]  # numbers that can be placed
    board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
    solve(board=board)
    for row in board:
        print(" ".join(row))