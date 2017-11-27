# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import sys
    import os
    import Simulate
    import ACO.ACO
    import Tool.AutoGenerate

    filepath = '/Users/joker/Documents/Code/GitHub/XY/Exp/test.txt'
    Tool.AutoGenerate.AutoGenerate.Generate(nodeSize=10, edgeSize=45, filepath=filepath)
    print 'generate finish'
    graph = Tool.AutoGenerate.AutoGenerate.Import(filepath)
    print graph.GetModularity()
    aco = ACO.ACO.ACO(antNumber=10, iterNumber=10, graph=graph, alpha=1, beta=1, roh=0.8, H=10)
    print 'begin run'
    aco.RunACO()