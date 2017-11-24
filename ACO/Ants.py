# -*- coding: utf-8 -*-

import os
import Simulate
from copy import deepcopy
from random import randint
from random import choice

class Ants(object):
    def __init__(self, graph, alpha, beta):
        '''
        init functon of Ants
        '''
        self._graph = deepcopy(graph)
        self._alpha = alpha
        self._beta = beta
        self._length = randint(1, len(self._graph._edge))
        self._currentPoint = choice(self._graph._edge)._startPoint
        self._path = [self._currentPoint]
        self._value = 0.0

    def MoveToNextEdge(self):
        for i in range(1, self._length):
            node = -1
            p = -1
            edge = None
            for e in self._graph._edge:
                if node == -1:
                    p = (e._pheromone ** self._alpha) * (e._display ** self._beta)
                    node = e._endPoint
                    edge = e
                elif e._startPoint == self._currentPoint and e._endPoint not in self._path:
                    if (e._pheromone ** self._alpha) * (e._display ** self._beta) > p:
                        p = e._pheromone
                        node = e._endPoint
                        edge = e
            if edge != None:
                self._path.append(node)
                self._currentPoint = node
                self._graph._edge.remove(edge)
            else:
                break

        # self._graph.UpdateDegree()
        self._value = self._graph.GetModularity()

    def ResetAnt(self, graph, alpha, beta):
        self._graph = deepcopy(graph)
        self._alpha = alpha
        self._beta = beta
        self._length = randint(1, len(self._graph._edge))
        self._currentPoint = choice(self._graph._edge)._startPoint
        self._path = [self._currentPoint]
        self._value = 0.0

    def IsPassEdge(self, startPoint, endPoint):
        if startPoint not in self._path or endPoint not in self._path:
            return False
        sp = self._path.index(startPoint)
        ep = self._path.index(endPoint)
        if abs(sp - ep) == 1:
            return True
        return False