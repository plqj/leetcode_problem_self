# 给你一个下标从 0 开始的二维整数数组 flowers
# 其中 flowers[i] = [starti, endi] 表示第 i 朵花的 花期 从 starti 到 endi （都 包含）
# 。同时给你一个下标从 0 开始大小为 n 的整数数组 people ，people[i] 是第 i 个人来看花的时间。
#
# 请你返回一个大小为 n 的整数数组 answer ，其中 answer[i]是第 i 个人到达时在花期内花的 数目 。

# 输入：flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]
# 输出：[1,2,2,2]


class Flower_Period(object):
    def __init__(self,flowers:list,people:list):
        self.flowers=flowers
        self.people=people

    def expand(self):
        """
        :return: a list that contains all the days
        """
        flowers_full=[]
        for i in self.flowers:
            l=[]
            for j in range(i[0],i[1]+1):
                l.append(j)
            flowers_full.append(l)

        return flowers_full

    def count(self,flower_full):
        out=[]
        for i in self.people:
            count=0
            for j in flower_full:
                if i in j:
                    count+=1
            out.append(count)
        return out

    def main(self):
        flower_full=self.expand()
        return self.count(flower_full=flower_full)


if __name__ == '__main__':
    flowers = [[1,10],[3,3]]
    people = [3,3,2]
    test=Flower_Period(flowers=flowers, people=people)
    print(test.main())