import random


class Node(object):
    """ 定义单链表节点类"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Graph(object):
    def __init__(self,V,E=None):
        """
        V:图的顶点数目
        E:图的边
        """
        self.V = list(range(int(V)))
        if E is None:
            self.E = [[0]*int(V) for _ in range(V)]

    def __repr__(self):
        string = ''
        for i in self.E:
            string += str(i) +'\n'
        # else:
        #     string.strip('\n')
            # print(string)
        return string
    
    def setEdges(self):
        """设置为无向图的邻接矩阵"""
        for i in range(len(self.V)):
            for j in range(i, len(self.V)):
                if i == j:
                    self.E[i][j] = 0
                else:
                    self.E[i][j] = self.E[j][i] = random.randrange(2)
        print(self,end = '')

    # def setEdgesofDirect(self):
    #     """设置为无向图的邻接矩阵"""
    #     for i in range(len(self.V)):
    #         for j in range(len(self.V)):
    #             if i == j:
    #                 G.E[i][j] = 0
    #             else:
    #                 G.E[i][j] = random.randrange(2)
    #     print(self,end = '')


if __name__ == "__main__":
    G = Graph(10)
    G.setEdges()
    pic = G.E
    print(pic)