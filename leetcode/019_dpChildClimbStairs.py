# 三步问题。有个小孩正在上楼梯，
# 楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。
# 实现一种方法，计算小孩有多少种上楼梯的方式。


def dpChildClimb(n):
    if n==1:return 1
    if n==2:return 2
    if n==3:return 4
    f_1,f_2,f_3=1,2,4
    for i in range(4,n+1):
        f=f_1+f_2+f_3
        f_1,f_2,f_3 = f_2,f_3,f
    return f_3

print(dpChildClimb(2))

