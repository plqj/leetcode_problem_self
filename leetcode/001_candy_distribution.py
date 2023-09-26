# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分
# 你需要按照以下要求，给这些孩了分发糖果:
# 每个孩子至少分配到 1 个糖果
# 相邻两个孩了评分更高的孩了会获得更多的糖果.
# 请你给每个孩了分发糖果，计算并返回需要准备的 最少糖果数目


class Candy(object):
    def __init__(self,ratings):
        self.ratings=ratings # input array
        self.reverse = self.ratings[::-1] # reversed array
        self.n = len(ratings) # how many children in need of candy
        self.forward_dist= [1] * self.n # initial candy distribution that satisfies "every child has a share", forward
        self.backward_dist=[1] * self.n # backward


    def forward(self):
        """
        :return: candy distribution that satisfies only forward requirement
        """
        for i in range(self.n-1):
            if self.ratings[i] < self.ratings[i+1]:
                self.forward_dist[i+1]=self.forward_dist[i]+1
        return self.forward_dist

    def backward(self):
        """
        :return: candy distribution that satisfies only backward requirement
        """
        for i in range(self.n-1):
            if self.reverse[i] < self.reverse[i+1]:
                self.backward_dist[i+1]=self.backward_dist[i]+1
        return self.backward_dist[::-1]

    def compare(self,l1,l2):
        l=[]
        for i in range(self.n):
            l.append(max(l1[i],l2[i]))
        return l

    def candy(self):
        l1=self.forward()
        l2=self.backward()
        l=self.compare(l1,l2)
        return sum(l)


if __name__ == "__main__":
    ratings=[1,0,2]
    test=Candy(ratings=ratings)
    print(test.candy())