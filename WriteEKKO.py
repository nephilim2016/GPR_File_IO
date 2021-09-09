#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:59:25 2021

@author: nephilim
"""

import numpy as np
import struct


def writeEKKO(file_name):
    headerFile=file_name+'.hd'
    filename=file_name+'.dt1'
    writeGPRhdr(headerFile)
    
    step_size=0.05
    sample=400
    scan=400
    
    data_input=np.load('data_input1.npy').astype('int16').transpose().flatten()
        
    with open(filename,'wb') as datafile:
        for idx in range(scan):
            head=struct.pack('32f',idx+1,step_size*idx,sample,0,0,2,200,16,0,0,0,\
                                 0,0,0,0,0,0,0,0,0,41,0,0,35248.1+idx,0,0,0,\
                                 0,0,0,0,0)
            datafile.write(head)
            for data_idx in range(sample):
                # print(idx*sample+data_idx)
                data=struct.pack('h',data_input[idx*sample+data_idx])
                datafile.write(data)
            
def writeGPRhdr(filename):
    with open(filename,'w') as fid:
        fid.write('1234\n')
        fid.write('Sys Config 1 - pulseEKKO v1.5.340\n')
        fid.write('2021-Sep-02\n')
        mat_int="{:<19s}= {:d}\n"
        mat_str="{:<19s}= {:s}\n"
        mat_float="{:<19s}= {:f}\n"

        fid.write(mat_int.format('NUMBER OF TRACES',400))
        fid.write(mat_int.format('NUMBER OF PTS/TRC',400))
        fid.write(mat_int.format('TIMEZERO AT POINT',41))
        fid.write(mat_int.format('TOTAL TIME WINDOW',80))
        fid.write(mat_float.format('STARTING POSITION',-0.00421034))
        fid.write(mat_float.format('FINAL POSITION',4.94579))
        fid.write(mat_float.format('STEP SIZE USED ',0.05))
        fid.write(mat_str.format('POSITION UNITS','m'))
        fid.write(mat_int.format('NOMINAL FREQUENCY',250))
        fid.write(mat_float.format('ANTENNA SEPARATION',0.4))
        fid.write(mat_int.format('PULSER VOLTAGE (V)',165))
        fid.write(mat_int.format('NUMBER OF STACKS',16))
        fid.write(mat_str.format('SURVEY MODE ','Reflection'))
        fid.write(mat_str.format('STACKING TYPE','F1, P16, DynaQ OFF'))
        fid.write(mat_str.format('TRIGGER MODE','Free'))
        fid.write(mat_str.format('DATA TYPE','F*4'))
        fid.write(mat_float.format('AMPLITUDE WINDOW (mV)',104.121822493))
        fid.write(mat_float.format('TRACE INTERVAL (s)',1.0))
        fid.write(mat_str.format('TRACEHEADERDEF_26','ORIENA'))
        fid.write(mat_str.format('GPR SERIAL#',''))
        fid.write(mat_str.format('RX SERIAL# ','002915901009'))
        fid.write(mat_str.format('DVL SERIAL#','0087-8086-2010'))
        fid.write(mat_str.format('TX SERIAL#','003015911007'))

if __name__=='__main__':
    file_name='lineTest1101'
    writeEKKO(file_name)