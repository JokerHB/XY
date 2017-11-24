# -*- coding: utf-8 -*-

class AutoGenerate(object):
    def __init__(self):
        '''
        init function of autogenerate
        '''
        pass

    @staticmethod
    def Generate(nodeSize, edgeSize, filepath):
        preList = ''
        listOfEdge = []
        from random import randint
        from random import random
        for i in range(edgeSize):
            sp = randint(0, nodeSize - 1)
            ep = randint(0, nodeSize - 1)
            while sp == ep or (sp, ep) in listOfEdge or (ep, sp) in listOfEdge:
                sp = randint(0, nodeSize - 1)
                ep = randint(0, nodeSize - 1)
            # preList.append((sp, ep, random()))
            preList += '%d\t%d\t%f\n' % (sp, ep, random())
            listOfEdge.append((sp, ep))
            listOfEdge.append((ep, sp))

        f = open(filepath, 'wb')
        f.write(preList)
        f.close()

    @staticmethod
    def Import(filepath):
        import re
        import Simulate.MyEdge
        import Simulate.BaseModel
        f = open(filepath, 'rb')
        content = f.readlines()
        f.close()
        partten = re.compile('(\d+)\t(\d+)\t(0\.\d+)')
        edges = []
        for l in content:
            info = partten.match(l)
            # print l
            # print info.group(0)
            if info != None:
                edge = Simulate.MyEdge.MyEdge(info.group(1), info.group(2), info.group(3))
                # edge = Simulate.MyEdge.MyEdge(info.group(2), info.group(1), info.group(3))
                edges.append(edge)
                # print info.group(1), info.group(2), info.group(3)
        # print len(edges)
        return Simulate.BaseModel.BaseModel(edge=edges)
