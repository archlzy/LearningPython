# M =   [2,2,0,5,3,5,7,4] # 列表中的数字代表队列1指向队列2的映射关系 队列1和队列2是一样的
#队列1：[a,b,c,d,e,f,g,h]
#队列2：[a,b,c,d,e,f,g,h]  #意味着M[1] 队列1中的a指向c
#目的找出 移动队列中的元素位置，使得最多的元素能够移动到指向的位置上，但是呢如果被指向的元素没有移动到他指向的元素上，是不可以移动的

input_list = [2,2,0,5,3,5,5,3,5,5,3,5]

# 递归的思路
def perm1(input_list, all_list = None):
    if all_list is None:
        all_list = set(range(len(input_list)))
    point_list = set(input_list[i] for i in all_list)
    unpoint_list = all_list - point_list
    if unpoint_list:
        del_item = unpoint_list.pop()
        all_list.remove(del_item)
        perm1(input_list, all_list)
    return all_list

def perm2(input_list):
    n = len(input_list)
    all_list = set(range(len(input_list)))
    count_list = [0]*n
    for i in input_list:
        count_list[i] += 1
    unpoint_list = [i for i in range(n) if count_list[i] == 0]
    while unpoint_list:
        del_item = unpoint_list.pop()
        all_list.remove(del_item)
        target_item = input_list[del_item]
        count_list[target_item] -= 1
        if count_list[target_item] ==0:
            unpoint_list.append(target_item)
    return all_list    
    

def perm3(input_list):
    record = []
    res = []
    for i,j in enumerate(input_list):
        if (i in record) or (i in res):
            continue
        templist = []
        while True:                             #队列1：[a,b,c,d,e,f,g,h]  [2,2,0,5,3,5,7,4]
            templist.append(i)
            if j in templist:
                flag = False
                for _i in templist:
                    if _i == j or flag:
                        flag = True
                        res.append(_i)
                    else:
                        record.append(_i)
                break
            i,j = j,input_list[j]
            if j in record:
                break
            if j in res:
                break
    return set(res)

import timeit

t1 = timeit.timeit(stmt = "perm1(input_list)", setup = 'from __main__ import perm1, input_list')
t2 = timeit.timeit(stmt = "perm2(input_list)", setup = 'from __main__ import perm2, input_list')
t3 = timeit.timeit(stmt = "perm3(input_list)", setup = 'from __main__ import perm3, input_list')
print(t1,t2,t3)

import random

test_list = [random.randint(0,99) for i in range(100)]
print(test_list)

# flag = (perm1(test_list) == perm2(test_list) == perm3(test_list))
# if flag:
#     print("结果一致")
#     # t1 = timeit.timeit(stmt = "perm1(test_list)", setup = 'from __main__ import perm1, test_list')
#     t2 = timeit.timeit(stmt = "perm2(test_list)", setup = 'from __main__ import perm2, test_list')
#     t3 = timeit.timeit(stmt = "perm3(test_list)", setup = 'from __main__ import perm3, test_list')
#     print(t2,t3)