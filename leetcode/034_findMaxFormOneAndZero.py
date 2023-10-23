# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
#
# 请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。
#
# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

# 输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
# 输出：4
# 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
# 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。


def allSearch(strs:list[str],m:int,n:int) -> int:
    dp = [[0] * (n + 1) for _ in range(m + 1)]  # 默认初始化0
    # 遍历物品
    for str in strs:
        ones = str.count('1')
        zeros = str.count('0')
        # 遍历背包容量且从后向前遍历！
        for i in range(m, zeros - 1, -1):
            for j in range(n, ones - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
    return dp[m][n]



if __name__ == '__main__':
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    print(allSearch(strs,m,n))