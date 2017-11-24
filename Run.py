# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import sys
    import os
    import Simulate
    import ACO.ACO
    import Tool.AutoGenerate

    filepath = '/Users/joker/Documents/Code/GitHub/XY/Exp/text_small.txt'
    # Tool.AutoGenerate.AutoGenerate.Generate(10, 30, filepath)
    # print 'generate finish'
    graph = Tool.AutoGenerate.AutoGenerate.Import(filepath)
    aco = ACO.ACO.ACO(antNumber=10, iterNumber=10, graph=graph, alpha=1, beta=1, roh=0.8, H=10)
    print 'begin run'
    aco.RunACO()