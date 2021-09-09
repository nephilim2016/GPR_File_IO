#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 15:51:36 2021

@author: nephilim
"""

import numpy as np

def readMALA(file_name):
    info=readGPRhdr(file_name+'.rad')
    try:
        filename=file_name+'.rd3'
        data=np.fromfile(filename,dtype=np.int16)        
    except:
        filename=file_name+'.rd7'
        data=np.fromfile(filename,dtype=np.int32)    
    nrows=int(len(data)/int(info['SAMPLES']))
    data=(np.asmatrix(data.reshape(nrows,int(info['SAMPLES'])))).transpose()
    return data,info

def readGPRhdr(filename):
    info={}
    with open(filename) as f:
        for line in f:
            strsp=line.split(':')
            info[strsp[0]]=strsp[1].rstrip()
    return info

if __name__=='__main__':
    file_name='WWL_025_0009_1'
    data,info=readMALA(file_name)