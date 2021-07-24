# -*- coding:utf-8 -*-
#Batch run any python script

import sys

def showHelp():
    print('python BatchRunAny.py userDefinedPythonProgram userDefinedPythonFunction config.txt')

def main():
    if(len(sys.argv)==1):
        showHelp()
        return

    pythonProgram=sys.argv[1]
    pythonFunction=sys.argv[2]
    batch_param_file=sys.argv[3]
    paramList=[]
    with open(batch_param_file,'r') as f:
        for line in f:
            paramList.append(line.strip().split(','))
    exec('from {} import {}'.format(pythonProgram,pythonFunction))

    for param in paramList:
        print('\n<---Batch running--->\nparam:{}'.format(param))
        param=','.join(param)
        eval('{}({})'.format(pythonFunction,param))

    print('Batch tasks finished!')

if __name__ == '__main__':
    main()


