# 给定一份单词的清单，设计一个算法，创建由字母组成的面积最大的矩形
# 其中每一行组成一个单词(自左向右)，每一列也组成一个单词(自上而下)。
# 不要求这些单词在清单里连续出现，但要求所有行等长，所有列等高。

# 如果有多个面积最大的矩形，输出任意一个均可。一个单词可以重复使用。

# 输入: ["this", "real", "hard", "trh", "hea", "iar", "sld"]
# 输出:
# [
#    "this",
#    "real",
#    "hard"
# ]


class Solution:
    def maxRectangle(self, words):
        from collections import defaultdict
        dictW, pre = defaultdict(set), set()
        for word in words:
            l = len(word)
            for i in range(1, l + 1):
                pre.add(word[: i])
            dictW[l].add(word)

        hts = sorted(dictW.keys(), reverse=True)
        self.res, self.mat, self.area = [''], [''], 0

        def check(ht, wd): # 判断终止条件
            if wd not in dictW or ht * wd <= self.area: # 宽度不在表里或者当前面积比已存在可能的最大面积小，直接返回
                return
            for line in self.mat:
                if ''.join(line) not in dictW[wd]: # 存在行单词不在词典的情况
                    return

            self.area = ht * wd
            self.res = [''.join(line) for line in self.mat]

        def dfs(ht):
            for word in dictW[ht]:
                getted = 1
                for i in range(ht):
                    self.mat[i].append(word[i])
                    s = ''.join(self.mat[i])
                    if s not in pre:
                        getted = 0
                        for j in range(i + 1):
                            self.mat[j].pop()
                        break

                if getted:
                    check(ht, len(self.mat[0]))
                    dfs(ht)
                    for j in range(ht):
                        self.mat[j].pop()

        for i in range(len(hts)):
            if self.res[0] and hts[i] ** 2 <= self.area:
                break

            self.mat = [[] for _ in range(hts[i])]
            dfs(hts[i])

        return len(self.res)*len(self.res[0]),self.res







if __name__ == '__main__':
    words = ["this", "real", "hard", "trh", "hea", "iar", "sld"]
    test = Solution()
    print(test.maxRectangle(words))


