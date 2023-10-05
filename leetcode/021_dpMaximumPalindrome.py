# 给你一个字符串 s，找到 s 中最长的回文子串。
#
# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
import copy


# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。


def dp_maximum(s:str):
    # 初始化动态规划
    n=len(s)
    dp = [["" for _ in range(n)] for _ in range(n)]

    # 长度为1的一定是回文
    for i in range(n):
        dp[i][i] = s[i]

    # 长度为2的相同字母回文
    for i in range(n-1):
        if s[i]==s[i+1]:
            dp[i][i+1]=s[i:i+2]

    flag=True
    dp_temp = copy.copy(dp)
    # 动态规划，转移方程为if语句内的内容
    while flag:
        for i in range(n):
            for j in range(i+2,n):
                if dp_temp[i+1][j-1] != "" and s[i]==s[j]:
                    dp_temp[i][j]=s[i:j+1]
        dp,dp_temp=dp_temp,dp
        if dp_temp == dp:
            flag=False

    # 计算最大长度
    m=0
    for i in range(n):
        for j in range(i,n):
            m=max(m,len(dp[i][j]))
    return dp,m


if __name__ == '__main__':
    s = "babaddddd"
    print(dp_maximum(s))