# length= 4 #图的边长

# Inf = float('inf')

# AdjecencyMatrix = [  # 给定的邻接矩阵
#     [  0,   1,   1, Inf],
#     [Inf,   0, Inf, Inf],
#     [  1, Inf,   0,   1],
#     [  1,   1,   1,   0]
# ]


# 点链表 双链表的形式
class ENode(object):
    """点链表，双链表形式，data：内容；firstin:入链接；firstout:出链接"""
    def __init__(self, data, firstin, firstout):
        self.Data = data
        self.Firstin = firstin
        self.Firstout = firstout
    
class VNode(object):
    """边链表，双链表形式，weight：权重；tailvex：尾指向, headvex：头指向, hlink：水平（正）链接, tlink：逆链接"""
    def __init__(self, tailvex, headvex, hlink, tlink):
        self.Tailvex = tailvex
        self.Headvex = headvex
        self.Hlink = hlink
        self.Tlink = tlink
        # self.Weight = weight

def InitData(length):
    ANodeList = []
    for i in range(length):
        ANodeList.append(ENode(i,None,None))
    return ANodeList

def setHlink():
    length  = len(ANodeList)
    for i in range(length):
        lastNode = None #i这一行暂时的空边或者上一个边
        for j in range(length):
            if AdjecencyMatrix[i][j] == 1: # i → j
                tempNode = VNode(i,j,None,None)
                if ANodeList[i].Firstout is None:
                    ANodeList[i].Firstout = tempNode
                    lastNode = ANodeList[i].Firstout 
                else:
                    lastNode.Hlink = tempNode
                    lastNode = lastNode.Hlink
            # if lastNode is not None:
            #     # print(id(lastNode), lastNode.__dict__)


def setTlink():
    def findVNode(j,i):
        for each in ANodeList:
            flag = each.Firstout
            while flag:
                if j == flag.Tailvex and i == flag.Headvex:
                    return flag
                flag = flag.Hlink

    length  = len(ANodeList)
    for i in range(length):
        lastNode = None #j这一列暂时的空边或者上一个边
        for j in range(length):
            if AdjecencyMatrix[j][i] == 1: # i → j
                tempNode =    findVNode(j,i)  #找到j，i 的节点 的边对象 存储到对应的点对象的位置
                if ANodeList[i].Firstin is None:
                    ANodeList[i].Firstin = tempNode
                    lastNode = ANodeList[i].Firstin 
                else:
                    lastNode.Tlink = tempNode
                    lastNode = lastNode.Tlink


def ShowCrossData(item):#展示十字链表的边，先试试横向的
        ItemFirstOut = item.Firstout
        print('vetex OUT:',end='')
        if ItemFirstOut==None:
            print('None')

        while(ItemFirstOut is not None):
            print(ItemFirstOut.Headvex,'->',ItemFirstOut.Tailvex,end='  ,   ')
            ItemFirstOut = ItemFirstOut.Hlink
        #下面是纵向输出
        ItemFirstIn  = item.Firstin
        print('vetex IN:', end='')
        if ItemFirstIn==None:
            print('None')

        while(ItemFirstIn is not None):
            print(ItemFirstIn.Headvex,'->',ItemFirstIn.Tailvex,end='  ,   ')
            ItemFirstIn = ItemFirstIn.Tlink



import 单链表

G= 单链表.Graph(10)
G.setEdges()
AdjecencyMatrix = G.E

length = len(AdjecencyMatrix)

for i in AdjecencyMatrix:
    print(i)



ANodeList = InitData(length)

setHlink()
setTlink()
for item in ANodeList:
    print('This is for node%2d:'%(item.Data))
    ShowCrossData(item)
    print('\n')


# This is for node 0:
# vetex OUT:1 -> 0  ,   2 -> 0  ,   vetex IN:0 -> 2  ,   0 -> 3  ,

# This is for node 1:
# vetex OUT:None
# vetex IN:1 -> 0  ,   1 -> 3  ,

# This is for node 2:
# vetex OUT:0 -> 2  ,   3 -> 2  ,   vetex IN:2 -> 0  ,   2 -> 3  ,

# This is for node 3:
# vetex OUT:0 -> 3  ,   1 -> 3  ,   2 -> 3  ,   vetex IN:3 -> 2  ,