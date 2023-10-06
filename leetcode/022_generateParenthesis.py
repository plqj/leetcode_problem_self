# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]

def generateParenthesis(n:int):
    if n <= 0: return []
    res = []

    def dfs(paths, left, right):
        if left > n or right > left: return
        if len(paths) == n * 2:  # 因为括号都是成对出现的
            res.append(paths)
            return

        dfs(paths + '(', left + 1, right)  # 生成一个就加一个
        dfs(paths + ')', left, right + 1)

    dfs('', 0, 0)
    return res



if __name__ == '__main__':
    n=3
    print(generateParenthesis(n))