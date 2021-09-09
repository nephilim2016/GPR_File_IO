#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Tue Sep  7 20:59:43 2021

@author: nephilim
'''

import struct
import numpy as np

def readEKKO(file_name):
    headerFile=file_name+'.hd'
    filename=file_name+'.dt1'
    info=readGPRhdr(headerFile)
    headlen=32
    with open(filename,'rb') as datafile:
        datafile.seek(8,0)
        samples,=struct.unpack('f',datafile.read(4))
        samples=int(samples)
        dimtrace=samples*2+128
        datafile.seek(-dimtrace,2)
        max_traces,=struct.unpack('f',datafile.read(4))
        max_traces=int(max_traces)
        data=np.zeros((samples,max_traces))
        head=np.zeros((headlen,max_traces))
        datafile.seek(0,0)
        for j in range(0,max_traces):
            for k in range(0,headlen):
                info_,= struct.unpack('f',datafile.read(4))
                head[k,j]=info_
            for k in range(0,samples):
                pnt,=struct.unpack('h',datafile.read(2))
                data[k,j]=pnt
            datafile.seek(dimtrace*(j+1),0) 
    return data,info

def readGPRhdr(filename):
    info={}
    with open(filename,'r',newline='\n') as datafile:
        datafile.readline().strip()
        info['system']=datafile.readline().strip()
        info['date']=datafile.readline().strip()
        alllines=datafile.readlines()
        for line in alllines:
            strsp=line.split('=')
            key=strsp[0].rstrip()
            info[key]=strsp[1].rstrip()
    return info

if __name__=='__main__':
    file_name='line1'
    file_name='lineTest1101'
    data,info=readEKKO(file_name)