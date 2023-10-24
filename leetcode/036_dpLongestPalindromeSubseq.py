# 给你一个字符串s ，找出其中最长的回文子序列，并返回该序列的长度。
#
# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
#
# 输入：s = "bbbab"
# 输出：4
# 解释：一个可能的最长回文子序列为
# "bbbb" 。


from functools import cache

class Solution:
    def longestPalindromeSubseq_dfs(self, s: str) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i > j: return 0  # 空串
            if i == j: return 1  # 只有一个字母
            if s[i] == s[j]:  # 都选
                return dfs(i + 1, j - 1) + 2
            return max(dfs(i + 1, j), dfs(i, j - 1))  # 枚举哪个不选 选择那个能给你带来最大利益可能性的。每一个都会算
        return dfs(0, len(s) - 1)

    def longestPalindromeSubseq_f(self, s: str) -> int:
        n = len(s)
        f = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            f[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])
            print(f)
        return f[0][-1]


if __name__ == '__main__':
    s="bbbab"
    solution=Solution()
    print(solution.longestPalindromeSubseq_dfs(s))
    print(solution.longestPalindromeSubseq_f(s))

