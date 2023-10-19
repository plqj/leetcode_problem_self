# 给你两个正整数 low 和 high ，都用字符串表示，请你统计闭区间 [low, high] 内的 步进数字 数目。
#
# 如果一个整数相邻数位之间差的绝对值都 恰好 是 1 ，那么这个数字被称为 步进数字 。
#
# 请你返回一个整数，表示闭区间 [low, high] 之间步进数字的数目。
#
# 由于答案可能很大，请你将它对 10^9 + 7 取余 后返回。
#
# 注意：步进数字不能有前导 0 。

# 输入：low = "90", high = "101"
# 输出：2
# 解释：区间 [90,101] 内的步进数字为 98 和 101 。总共有 2 个步进数字。所以输出为 2 。

from functools import cache


def dpDigitTypeCountSteppingNumber(low:str,high:str)->int:
    MOD = 10 ** 9 + 7

    def inner(s: str) -> int:
        @cache  # 记忆化搜索
        def f(i: int, pre: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):return int(is_num)  # is_num 为 True 表示得到了一个合法数字
            res = 0
            if not is_num:res = f(i + 1, pre, False, False)
            low = 0 if is_num else 1  # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
            up = int(s[i]) if is_limit else 9  # 如果前面填的数字都和 s 的一样，那么这一位至多填 s[i]（否则就超过 s 啦）
            for d in range(low, up + 1):  # 枚举要填入的数字 d
                if not is_num or abs(d - pre) == 1:  # 第一位数字随便填，其余必须相差 1
                    res += f(i + 1, d, is_limit and d == up, True)
            return res % MOD

        return f(0, 0, True, False)

    return (inner(high) - inner(str(int(low) - 1))) % MOD



if __name__ == '__main__':
    low="98"
    high="101"
    print(dpDigitTypeCountSteppingNumber(low,high))