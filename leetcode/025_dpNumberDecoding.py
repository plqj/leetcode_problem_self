# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
#
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）

# 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
#
# 题目数据保证答案肯定是一个 32 位 的整数。


# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6)

def numDecodings(s: str) -> int:
    if s.startswith('0'):  # 开头有 ‘0’ 直接返回
        return 0

    n = len(s)
    dp = [1] * (n+1)  # 重点是 dp[0], dp[1] = 1, 1

    for i in range(2, n+1):
        if s[i-1] == '0' and s[i-2] not in '12':  # 出现前导 ‘0’ 的情况，不能解码，直接返回
            return 0
        if s[i-2:i] in ['10', '20']:  # 只有组合在一起才能解码
            dp[i] = dp[i-2]
        elif '10' < s[i-2:i] <= '26': # 两种解码方式
            dp[i] = dp[i-1] + dp[i-2]
        else:                         # '01'到 ‘09’ 或 > '26'，只有单独才能解码
            dp[i] = dp[i-1]
    return dp[n]


if __name__ == '__main__':
    s="226"
    print(numDecodings(s))