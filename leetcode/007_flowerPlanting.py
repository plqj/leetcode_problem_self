# 假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。
# 可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
#
# 给你一个整数数组 flowerbed 表示花坛，由若干 0 和 1 组成
# 其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花
# 能则返回 true ，不能则返回 false


class Flower_Planting(object):
    def __init__(self,board,n):
        self.board=board
        self.n=n

    def expanding(self):
        """
        expanding the input flower board with 0 both at the beginning and ending place
        :return: expanded board
        """
        self.board.append(0)
        self.board.insert(0,0)
        return self.board

    def simulate(self):
        """
        simulate the planting process, skip the expanded first and last element; skip the place already in plant; check if the candidate place has no neighbors.
        :return: how many flowers can be put in without violation against rules at maximum
        """
        count=0
        for i in range(len(self.board)):
            if i == 0 or i == len(self.board)-1:
                continue

            if self.board[i]==1:
                continue

            else:
                if self.board[i-1] == 0 and self.board[i+1]==0:
                    self.board[i]=1
                    count+=1
                else:
                    continue
        return count

    def compare(self,t):
        """
        :param t: result in self.simulation()
        :return: True or False
        """
        if self.n<=t:
            return True
        else:
            return False

    def main(self):
        self.expanding()
        out=self.simulate()
        result=self.compare(out)
        return result


if __name__ == '__main__':
    board=[0,0,0,1,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1]
    n=6
    test=Flower_Planting(board=board,n=n)
    print(test.main())


