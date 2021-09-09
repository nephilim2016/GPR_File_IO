#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 18:26:02 2021

@author: nephilim
"""

import struct
import numpy as np
import datetime

def writeGSSI(filename):    
    # H is unsigned int 16 (ushort = uint16)
    # h is short (int16)
    # I is unsigned int 32 (uint = uint32)
    # i is int32
    # f is float
    # c is char
    # s is char[]
    info={}
    info['rh_tag']=2047
    info['rh_data']=128
    info['rh_nsamp']=1024
    info['rh_bits']=32
    
    info['rh_zero']=6
    
    info['rh_sps']=100.0
    info['rh_spm']=200.0
    info['rh_mpm']=0.0
    info['rh_position']=-8.88888
    info['rh_range']=88.8888931274414
    
    info['rh_npass']=0
    
    info['rh_create']=' '*4
    info['rh_modif']=' '*4
    
    info['rh_rgain']=2048
    info['rh_nrgain']=7
    info['rh_text']=512
    info['rh_ntext']=0
    info['rh_proc']=128
    info['rh_nproc']=6
    info['rh_nchan']=1
    
    info['rh_epsr']=9.0
    info['rh_top']=0.444444477558136
    info['rh_depth']=3e8/(np.sqrt(info['rh_epsr']))*info['rh_range']*1e-9/2
    
    info['rh_reserved']=' '*18
    info['rh_spp']=1
    info['rh_linemun']=0
    info['rh_start_x']=0
    info['rh_start_y']=0
    info['rh_end_x']=0
    info['rh_end_y']=0
    info['rh_lineorder']=' '
    info['rh_dtype']=' '
    info['rh_antname']='%14s'%'50400S'
    info['rh_chanmask']=16384
    info['rh_name']='            '
    info['rh_chksum']=0
    info['rh_variable']=' '*896
    
    info['rh_create']=info['rh_create'].encode('ascii')
    info['rh_modif']=info['rh_modif'].encode('ascii')
    info['rh_reserved']=info['rh_reserved'].encode('ascii')
    info['rh_lineorder']=info['rh_lineorder'].encode('ascii')
    info['rh_dtype']=info['rh_dtype'].encode('ascii')
    info['rh_antname']=info['rh_antname'].encode('ascii')
    info['rh_name']=info['rh_name'].encode('ascii')
    info['rh_variable']=info['rh_variable'].encode('ascii')
    with open(filename,'wb') as fid:
        minheadsize=1024
        DZT_HEADER_STRUCT='=4Hh5fH4s4s7H3f18s2H4hcc14sH12sh896s'
        head=struct.pack(DZT_HEADER_STRUCT,
                         info['rh_tag'],
                         info['rh_data'],
                         info['rh_nsamp'],
                         info['rh_bits'],
                         info['rh_zero'],
                         info['rh_sps'],
                         info['rh_spm'],
                         info['rh_mpm'],
                         info['rh_position'],
                         info['rh_range'],
                         info['rh_npass'],
                         info['rh_create'],
                         info['rh_modif'],
                         info['rh_rgain'],
                         info['rh_nrgain'],
                         info['rh_text'],
                         info['rh_ntext'],
                         info['rh_proc'],
                         info['rh_nproc'],
                         info['rh_nchan'],
                         info['rh_epsr'],
                         info['rh_top'],
                         info['rh_depth'],
                         info['rh_reserved'],
                         info['rh_spp'],
                         info['rh_linemun'],
                         info['rh_start_x'],
                         info['rh_start_y'],
                         info['rh_end_x'],
                         info['rh_end_y'],
                         info['rh_lineorder'],
                         info['rh_dtype'],
                         info['rh_antname'],
                         info['rh_chanmask'],
                         info['rh_name'],
                         info['rh_chksum'],
                         info['rh_variable'])
        fid.write(head)
        
        data_input=np.load('testGSSIData.npy')
        nsample=info['rh_nsamp']
        nscan=data_input.size//nsample
        data_input[0,:]=np.arange(nscan)+1
        data_input=data_input.astype('int32').transpose().flatten()
        
        fid.seek(minheadsize*(info['rh_data']),0) 
        # fid.write(bytes(minheadsize*(info['rh_data']-1)))
        
        for idx in range(nscan):
            for data_idx in range(nsample):
                data=struct.pack('i',data_input[idx*nsample+data_idx])
                fid.write(data)

if __name__=='__main__':
    filename='Test1.DZT'
    writeGSSI(filename)