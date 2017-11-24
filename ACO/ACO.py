# -*- coding: utf-8 -*-

class ACO(object):
    def __init__(self, antNumber, iterNumber, graph, alpha, beta, roh, H):
        '''
        init function of _ACO
        '''
        self._antNumber = antNumber
        self._iterNumber = iterNumber
        self._graph = graph
        self._alpha = alpha
        self._beta = beta
        self._roh = roh
        self._H = H

    def RunACO(self):
        import Ants

        antList = []
        for _ in range(self._antNumber):
            antList.append(Ants.Ants(graph=self._graph, alpha=self._alpha, beta=self._beta))

        for _ in range(self._iterNumber):
            # print _
            for ant in antList:
                ant.MoveToNextEdge()

            for edge in self._graph._edge:
                edge._pheromone = self._roh * edge._pheromone
                delta = 0.0
                for ant in antList:
                    if ant.IsPassEdge(edge._startPoint, edge._endPoint):
                        delta += self._H / ant._value
                edge._pheromone += delta

            sum_phe = map(lambda x: x._pheromone, self._graph._edge)
            # print sum_phe
            sum_phe = sum(sum_phe)
            # print sum_phe
            for edge in self._graph._edge:
                edge._pheromone /= sum_phe
            # sum_phe = map(lambda x: x._pheromone, self._graph._edge)
            # print sum_phe

            for ant in antList:
                ant.ResetAnt(graph=self._graph, alpha=self._alpha, beta=self._beta)

        # print antList
        best = antList[0]
        for i in range(1, len(antList)):
            if antList[i]._value >= best._value:
                best = antList[i]

        print best._value
        print best._path
