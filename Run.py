# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import sys
    import os
    import Simulate
    import Tool.AutoGenerate

    filepath = '/Users/joker/Documents/Code/GitHub/XY/Exp'
    # Tool.AutoGenerate.AutoGenerate.Generate(20, 30, filepath + '/text.txt')
    Tool.AutoGenerate.AutoGenerate.Import(filepath + '/text.txt')
