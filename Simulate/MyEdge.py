# -*- coding: utf-8 -*-

class MyEdge(object):
    def __init__(self, startPoint, endPoint, weight, pheromone = 1., display = 1.):
        '''
        init function of MyEdge
        '''
        self._startPoint = startPoint
        self._endPoint = endPoint
        self._weight = float(weight)
        self._pheromone = pheromone
        self._display = display
