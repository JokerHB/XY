# -*- coding: utf-8 -*-

class BaseNode(object):
    def __init__(self, value):
        '''
        init function of BaseNode
        '''
        self._value = value
        self._father = self
        self._rank = 1

class UnionSet(object):
    def __init__(self):
        '''
        init function of Union Set Operation
        '''
        pass

    def Find(self, nodeA):
        if nodeA._father != nodeA:
            nodeA._father = self.Find(nodeA._father)
        return nodeA._father

    def Union(self, nodeA, nodeB):
        fa = self.Find(nodeA)
        fb = self.Find(nodeB)

        if fa != fb:
            if fa._rank >= fb._rank:
                fa._rank += fb._rank
                nodeB._father = nodeA
            else:
                fb._rank += fa._rank
                nodeA._father = nodeB