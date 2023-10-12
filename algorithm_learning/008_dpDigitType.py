# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
# 如果计算0出现的次数呢？

from functools import cache

def count1(n:int) ->int:
    # 将n转化为字符串
    s=str(n)

    @cache # 很必要，不然递归太多会超时
    def f(i,cnt1,isLimit:bool):
        """
        :param i:表示构造到从左往右第i位
        :param cnt1: 在第i位时已经出现的‘1’的个数 最终要输出的结果
        :param isLimit: 表示当前是否受到了n的约束。若为真，则第i位最多填到s[i]，否则可以到9。如果在受到约束的情况下填的s[i]，后续也要受约束
        :param isNum:表示i前面的数位是否填了数字，若为假，则当前位可以跳过，或者至少要从1开始填，若为真，则要填入的数字可以从0开始
        :return:
        """
        # 后面两个参数可适用于其它数位 DP 题目
        # 对于本题来说，由于前导零对答案无影响，isNum可以省略。

        if i == len(s):
            return cnt1 # 如果已经迭代到了最后一位，则直接打印结果
        res = 0
        up = int(s[i]) if isLimit else 9
        for d in range(up + 1):  # 枚举要填入的数字 d
            res += f(i + 1, cnt1 + (d == 1), isLimit and d == up)
        return res

    return f(0, 0, True)


def count0(n:int) ->int:
    # 将n转化为字符串
    s=str(n)

    @cache
    def f(i,cnt1,isLimit:bool,isNum:bool):
        """
        :param i:表示构造到从左往右第i位
        :param cnt1: 在第i位时已经出现的‘1’的个数 最终要输出的结果
        :param isLimit: 表示当前是否受到了n的约束。若为真，则第i位最多填到s[i]，否则可以到9。如果在受到约束的情况下填的s[i]，后续也要受约束
        :param isNum:表示i前面的数位是否填了数字，若为假，则当前位可以跳过，或者至少要从1开始填，若为真，则要填入的数字可以从0开始
        :return:
        """
        # 后面两个参数可适用于其它数位 DP 题目

        if i == len(s):
            return cnt1 # 如果已经迭代到了最后一位，则直接打印结果
        res = 0

        if not isNum:
            res+=f(i+1,cnt1,False,False)

        up = int(s[i]) if isLimit else 9
        for d in range(1-int(isNum),up + 1):  # 枚举要填入的数字 d，这里要分类讨论，如果前面没构成数字，则要用1开始试验，若已经构成了，则从零开始
            res += f(i + 1, cnt1 + (d == 0), isLimit and d == up,True)
        return res

    return f(0, 0, True,False)


if __name__ == '__main__':
    n=25
    print(count1(n))
    # 以数字13为例，首先调用了
    # f(i=0,cnt1=0,isLimit=True) # 初始化了这一层的res_0=0 计算发现up_0要等于1，也就是说，第一位是受到限制的，只能取0和1，将0和1循环赋值给d_0，对于0而言，调用
    #   # f(i=1,cnt1=0,isLimit=False) # 考虑到数字d_0此时为零,cnt1_1=0，不等于up_0，也就是说这一位随便取。初始化res_10=0，up_10=9，数字d_1的取值可以从0到9循环填入，调用
    #   #   # f(i=2,cnt1=0,isLimit=False) # d_1此时为零，cnt1_2仍是零，isLimit此时不重要，发现符合if内条件，直接return cnt1_2的值0，加等到res_10上
    #   #   # f(i=2,cnt1=1,isLimit=False) # d_1此时为1，cnt1_2为1，isLimit此时不重要，发现符合if内条件，直接return cnt1_2的值1，加等到res_10上
    #   #   # f(i=2,cnt1=0,isLimit=False) # d_1此时为2，cnt1_2仍是零，isLimit此时不重要，发现符合if内条件，直接return cnt1_2的值0，加等到res_10上
    #   #   #   # 能发现，d_1为零和2的时候传入的参数是一样的，所以用装饰器@cache可以直接得到cnt1_2的值为0，直接return出来就好，不用重复调用计算，以空间换时间。
    #   #   # 以此类推，直到d_1循环完，res_10为1，return res_10加等到res_0上，f(i=1,cnt1=0,isLimit=False)执行完毕
    #   # f(i=1,cnt1=1,isLimit=True) # 考虑到数字d_0此时为1，cnt1_1=1(因为d==1)，d_0==1与up_0相等，也就是这一位是受限制的，初始化res_11=0,up_11=3,d_1只能取到[0,3]闭区间,调用
    #   #   # f(i=2,cnt1=1,isLimit=False) # d_1此时为零，cnt1_2=1(因为d==0)，isLimit此时不重要，发现符合if内条件，直接return cnt1_2值为1，加等到res_11上
    #   #   # f(i=2,cnt1=2,isLimit=False) # d_1此时为1，cnt1_2=2(因为d==1)，isLimit此时不重要，发现符合if内条件，直接return cnt1_2值为2，加等到res_11上
    #   #   # f(i=2,cnt1=1,isLimit=False) # d_1此时为2，cnt1_2=1(因为d==2)，isLimit此时不重要，发现符合if内条件，直接return cnt1_2值为1，加等到res_11上
    #   #   # f(i=2,cnt1=1,isLimit=True) # d_1此时为3，cnt1_2=1(因为d==3)，isLimit此时不重要，发现符合if内条件，直接return cnt1_2值为1，加等到res_11上
    #   #   # 循环完发现res_11等于5，return res_11加等到res_0上，f(i=1,cnt1=1,isLimit=True)执行完毕
    #   # 最开始的f(i=0,cnt1=0,isLimit=True)执行完毕，res_0 == res_10+res_11 == 6，输出res

    print(count0(n))



