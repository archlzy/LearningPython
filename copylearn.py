W = 4#图的边长
INF = float('inf')
Pic = [[0, 1,  1 ,INF],
       [INF,0,INF,INF],
       [1,INF,  0,  1],
       [1, 1,   1, 0]]
ANodeList = []
class ANode:#顶点
    def __init__(self,data,firstin,firstout):
        self.Data = data
        self.Firstin = firstin
        self.Firstout  = firstout
class VNode:#边
    def __init__(self,tailvex,headvex,hlink,tlink,weight):
        self.Tailvex = tailvex
        self.Headvex = headvex
        self.Hlink = hlink
        self.Tlink = tlink
        self.Weight = weight
def InitData():
    #还是用index来初始化data吧
    for i in range(W):
        newnode = ANode(i,None,None)
        ANodeList.append(newnode)
def HorizontalLink():#横向联系
    for i in range(len(ANodeList)):
        ptail = VNode(None,None,None,None,None)
        #搞一个尾指针
        for j in range(W):#查找firstout
            if Pic[i][j]==1:
                NewVect = VNode(j, ANodeList[i].Data, None, None, 10)
                if ANodeList[i].Firstout==None:#如果是头指针为空,就赋予第一个找到的出度边
                    ANodeList[i].Firstout = NewVect
                    ptail = ANodeList[i].Firstout#tail指向头
                else:
                    ptail.Hlink = NewVect
                    ptail = NewVect
def SearchForVNode(head,tail):#这是为了在纵向联系时能找到对应的节点
    for each in ANodeList:
        tempVNode = each.Firstout
        while (tempVNode !=None ):
            if tempVNode.Headvex==head and tempVNode.Tailvex==tail:
                return tempVNode
            else:
                tempVNode = tempVNode.Hlink

     #正常情况下应该不会返回None
def VerticalLink():#纵向联系
    for i in range(len(ANodeList)):
        ptail = VNode(None, None, None, None, None)
        for j in range(W):
            if Pic[j][i]==1:#这次要竖着来
                if ANodeList[i].Firstin==None:

                    ANodeList[i].Firstin=SearchForVNode(j,i)
                    ptail = ANodeList[i].Firstin
                else:
                    SearchRes = SearchForVNode(j,i)
                    ptail.Tlink = SearchRes
                    ptail = SearchRes

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

if __name__=='__main__':
    InitData()
    HorizontalLink()
    VerticalLink()
    for item in ANodeList:
        print('This is for node%2d:'%(item.Data))
        ShowCrossData(item)
        print('\n')
    
