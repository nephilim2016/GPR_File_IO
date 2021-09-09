#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 10:14:14 2021

@author: nephilim
"""


import struct
import numpy as np
import datetime

def dzt_headers_datetime(date_bytes):
    binary_array = format(struct.unpack("=I", date_bytes)[0], "b").zfill(32)[::-1]
    sec2=int(binary_array[0:5][::-1], base=2)  # 5-bits 00-04  0-29 (second/2)
    minutes=int(binary_array[5:11][::-1], base=2)  # 6-bits 05-10  0-59
    hour=int(binary_array[11:16][::-1], base=2)  # 5-bits 11-15  0-23
    day=int(binary_array[16:21][::-1], base=2)  # 5-bits 16-20  1-31
    month=int(binary_array[21:25][::-1], base=2)  # 4-bits 21-24  1-12, 1=Jan, 2=Feb, etc.
    year=int(binary_array[25:32][::-1], base=2)  # 7-bits 25-31  0-127 (0-127 = 1980-2107)
    value_range_pairs=((sec2,(0,30)),(minutes,(0,60)),(hour,(0,24)),(day, (1,32)),(month,(1,13)),(year,(0,128)))

    if all((v >= lb) & (v < ub) for v, (lb, ub) in value_range_pairs):
        return datetime.datetime(1980 + year, month, day, hour, minutes, sec2 * 2)
    else:
        return '%s-%s-%s %s:%s:%s'%(year+1980,month,day,hour,minutes,sec2*2)
    
def readGSSI(filename):    
    # H is unsigned int 16 (ushort = uint16)
    # h is short (int16)
    # I is unsigned int 32 (uint = uint32)
    # i is int32
    # f is float
    # c is char
    # s is char[]
    info={}
    with open(filename,'rb') as fid:
        minheadsize=1024
        header=fid.read(minheadsize)
        DZT_HEADER_STRUCT='=4Hh5fH4s4s7H3f18s2H4hcc14sH12sh896s'
        (info['rh_tag'],
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
         info['rh_variable'])=struct.unpack(DZT_HEADER_STRUCT,header)
        info['rh_tag_bits']=hex(info['rh_tag'])
        info['rh_tag_bytes']=struct.pack("H",info['rh_tag']).decode('ascii','ignore').replace("\x00", " ").strip()
        info['rh_create_time']=dzt_headers_datetime(info['rh_create'])
        info['rh_modif_time']=dzt_headers_datetime(info['rh_modif'])
        info['rh_reserved']=info['rh_reserved'].decode('ascii','ignore').replace("\x00", " ").strip()
        info['rh_lineorder']=info['rh_lineorder'].decode('ascii','ignore').replace("\x00", " ").strip()
        info['rh_dtype']=info['rh_dtype'].decode('ascii','ignore').replace("\x00", " ").strip()
        info['rh_antname']=info['rh_antname'].decode('ascii','ignore').replace("\x00", " ").strip()
        info['rh_name']=info['rh_name'].decode('ascii','ignore').replace("\x00", " ").strip()
        info['rh_variable']=info['rh_variable'].decode('ascii','ignore').replace("\x00", " ").strip()
        if info['rh_data']!=1024:
            fid.read(minheadsize*(info['rh_data']-1))
        else:
            fid.read(minheadsize*(info['rh_nchan']-1))
        if info['rh_bits']==8:
            datatype='uint8'
        elif info['rh_bits']==16:
            datatype='uint16'
        elif info['rh_bits']==32:
            datatype='int32'
        data=np.fromfile(fid,dtype=datatype)
        nsample=info['rh_nsamp']
        nscan=data.size//nsample
        data=data.reshape((nscan,nsample)).transpose()
        data[:2,:]=0
    return data,info

if __name__=='__main__':
    # filename='HX1110__010.DZT'
    # filename='CSU1215__006.DZT'
    filename='Test1.DZT'
    data,info=readGSSI(filename)