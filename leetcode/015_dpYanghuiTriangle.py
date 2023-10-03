# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
#
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。

# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


class DPTriangle(object):
    def __init__(self,numRows):
        self.numRows=numRows
        self.dp=[[0]*self.numRows for _ in range(self.numRows)]
        for j in range(self.numRows):
            self.dp[j][0]=1

    def triangle(self):
        for row in range(1,self.numRows):
            for col in range(1,self.numRows):
                self.dp[row][col]=self.dp[row-1][col]+self.dp[row-1][col-1]
        for row in range(self.numRows):
            self.dp[row]=list(filter(lambda x: x != 0, self.dp[row]))
        return self.dp




if __name__ == '__main__':
    numRows=1
    test=DPTriangle(numRows)
    print(test.triangle())