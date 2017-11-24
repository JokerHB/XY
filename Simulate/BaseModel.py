# -*- coding: utf-8 -*-

from MyEdge import MyEdge
from copy import deepcopy

class BaseModel(object):
    def __init__(self, edge):
        '''
        init function of BaseModel
        '''

        self._edge = deepcopy(edge)
        self._node = []
        self._cluster = []
        self._modularity = 0.0
        self._degree = {}
        self._m = 0.0

        for e in self._edge:
            if e._startPoint not in self._node:
                self._node.append(e._startPoint)
            if e._endPoint not in self._node:
                self._node.append(e._endPoint)
            try:
                self._m += e._weight
            except Exception, t:
                print type(e._weight)


    def SumWeightOfUV(self, startPoint, endPoint):
        if len(self._edge) == 0:
            return 0
        ans = 0
        for e in self._edge:
            if e._startPoint == startPoint and e._endPoint == endPoint:
                ans += e._weight
                break
        return ans

    def SumWeightOfGraph(self):
        if len(self._edge) == 0:
            return 0
        ans = 0
        for e in self._edge:
            ans += e._weight
        self._m = ans
        # return ans / 2.0

    def UpdateDegree(self):
        self._degree = {}
        for e in self._edge:
            if e._startPoint in self._degree:
                self._degree[e._startPoint] += e._weight
            else:
                self._degree[e._startPoint] = e._weight

    def UpdateCluster(self):
        import Tool.UnionSet

        unionSet = Tool.UnionSet.UnionSet()
        nodelist = []

        for _ in self._node:
            nodelist.append(Tool.UnionSet.BaseNode(value=_))

        for e in self._edge:
            na = nodelist.index(e._startPoint)
            nb = nodelist.index(e._endPoint)
            unionSet.Union(nodelist[na], nodelist[nb])

        # self._cluster = {}
        #
        # for _ in nodelist:
        #     fa = unionSet.Find(_)
        #     if fa not in self._cluster:
        #         self._cluster[fa] = [_]
        #     else:
        #         if _ not in self._cluster[fa]:
        #             self._cluster[fa].append(_)
        #
        # print self._cluster

    def JudgeSameCluster(self, nodeA, nodeB):
        import Tool.UnionSet

        unionSet = Tool.UnionSet.UnionSet()

        if unionSet.Find(nodeA) == unionSet.Find(nodeB):
            return True
        return False

    def GetModularity(self):
        self.UpdateDegree()
        self.UpdateCluster()
        self._modularity = 0.0
        for i in self._node:
            for j in self._node:
                if i != j and self.JudgeSameCluster(i, j):
                    aij = self.SumWeightOfUV(startPoint=i, endPoint=j)
                    self._modularity += aij - ((self._degree[i] * self._degree[j]) / (2.0 * self._m))
        self._modularity /= (2.0 * self._m)
        return self._modularity