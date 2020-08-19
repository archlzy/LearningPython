# class Tree: # 二叉树类
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right

# class Tree: # 多路搜索树类
#     def __init__(self, kids, next=None):
#         self.kids = self.val = kids
#         self.next = next

# class Bunch(dict):
#     def __init__(self, *args, **kargs):
#         super().__init__(self, *args, **kargs)
#         self.__dict__ = self

import random
import timeit

test_list=  [random.randint(10,100) for i in range(900)]

def func1(seq, i=0):
    if i == len(seq): return 0
    return func1(seq, i+1) +seq[i]
    
def func2(seq):
    sum_num = 0
    for i in test_list:
      sum_num += i
    return sum_num

func3 = sum

# t1 = timeit.timeit("func1(a_list)",setup = "import random;a_list = [random.randint(10,100) for i in range(360)]; from __main__ import func1", number=10)
t2 = timeit.timeit("func2(a_list)",setup = "import random;a_list = [random.randint(1,10) for i in range(3600000)]; from __main__ import func2", number=10)
t3 = timeit.timeit("func3(a_list)",setup = "import random;a_list = [random.randint(10,100) for i in range(3600000)]; from __main__ import func3", number=10)
print(t2,t3)
# 0.00021956799999999985 0.0003265520000000008 8.397000000000265e-06
# 0.0004518870000000015 0.00034365800000000363 1.5239000000000225e-05
# 0.0010287959999999985 0.00033183900000000044 3.1099999999999184e-05
#                       0.00033836999999999756 0.000300118000000002
#                       0.00033401699999996426 0.02794355999999998