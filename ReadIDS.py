#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:17:35 2021

@author: nephilim
"""

import struct
import numpy as np

def readIDS(filename): 
    info={}

    with open('LZZ10001.dt','rb') as fid:
        code,=struct.unpack('1s',fid.read(1))
        code=code.decode('ascii','ignore')

        file_version,=struct.unpack('h',fid.read(2))
        fid.read(1)

        len_rec,=struct.unpack('h',fid.read(2))
        pos=len_rec

        while True:
            fid.seek(pos,0)
            stop_tmp,=struct.unpack('4s',fid.read(4))
            stop_key=stop_tmp.decode('ascii','ignore').replace("\x00", " ").replace("\x15", " ").replace("\x04", " ").strip()
    
            if stop_key=='FI':
                data_tmp,=struct.unpack('6s',fid.read(6))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['sweep_marker_1']=data_key
        
            if stop_key=='I':
                data_tmp,=struct.unpack('%ss'%(len_rec-4),fid.read(len_rec-4))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['survey_info']=data_key
        
            if stop_key=='C':
                data_tmp,=struct.unpack('%ss'%(len_rec-4),fid.read(len_rec-4))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['survey_time']=data_key
    
            if stop_key=='AH':
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['height']=data_key
        
            if stop_key=='FZ':
                data_tmp,=struct.unpack('%ss'%(len_rec-4),fid.read(len_rec-4))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['zone']=data_key
        
            if stop_key=='FX':
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['offset_x']=data_key
        
            if stop_key=='FQ':
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['marker_quantum']=data_key
        
            if stop_key=='FM':
                data_tmp,=struct.unpack('6s',fid.read(6))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['sweep_marker']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['position']=data_key
        
            if stop_key=='AC1':
                data_tmp,=struct.unpack('i',fid.read(4))
                info['tx_n']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['tx_seq']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['rx_n']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['rx_seq']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['nacq']=data_tmp
        
            if stop_key=='AM':
                data_tmp,=struct.unpack('1s',fid.read(1))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['direct']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['coord_l']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['coord_t']=data_key
                
            if stop_key=='ATR':
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['tx_x0']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['tx_y0']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['tx_alpha']=data_key
                data_tmp,=struct.unpack('5s',fid.read(5))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['tx_freq']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['rx_x0']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['rx_y0']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['rx_alpha']=data_key
                data_tmp,=struct.unpack('5s',fid.read(5))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['rx_freq']=data_key
        
        
            if stop_key=='ATX':
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['tx_x0']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['tx_y0']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['tx_alpha']=data_key
                data_tmp,=struct.unpack('5s',fid.read(5))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['tx_freq']=data_key
        
            if stop_key=='AA':
                data_tmp,=struct.unpack('%ss'%(len_rec-4),fid.read(len_rec-4))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['info']=data_key
        
            if stop_key=='S':
                data_tmp,=struct.unpack('%ss'%(len_rec-4),fid.read(len_rec-4))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['S']=data_key
                
            if stop_key=='FW':
                data_tmp,=struct.unpack('i',fid.read(4))
                info['da_buttare']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['channel_n']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['stacking']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['interleaving']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['channel_id']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['SOS_high']=data_tmp
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['sampling_max']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['sw_version']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['build_version']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['fw_version']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['GPS_offset_x']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['GPS_offset_y']=data_key
        
            if stop_key=='H':
                data_tmp,=struct.unpack('i',fid.read(4))
                info['scratch']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['n_acq_sweep']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['n_acq_sample']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['n_sampler_x']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['n_sampler_y']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['enable_x_compress']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['n_x_compress']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['n_y_compress']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['enable_wheel']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['wheel_compress']=data_tmp
                data_tmp,=struct.unpack('i',fid.read(4))
                info['ad_offset']=data_tmp
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['radar_freq']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['prop_vel']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['sweep_time']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['sweep_time_tot']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['scan_freq']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['scan_time_acq']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['sweep_dx']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['wheel_dx']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['x_cell']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['y_cell']=data_key
    
            if stop_key=='FC':
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['conv_int_volts']=data_key
        
            if stop_key=='FS':
                data_tmp,=struct.unpack('%ss'%(len_rec-4),fid.read(len_rec-4))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['direct']=data_key

            if stop_key=='FT':
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['t_soil_sample']=data_key
        
            if stop_key=='FO':
                data_tmp,=struct.unpack('%ss'%(len_rec-4),fid.read(len_rec-4))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['info_operation']=data_key
        
            if stop_key=='FN':
                data_tmp,=struct.unpack('i',fid.read(4))
                info['id_sample_noise']=data_tmp

            if stop_key=='ARX':
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['rx_x0']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['rx_y0']=data_key
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['rx_alpha']=data_key
                data_tmp,=struct.unpack('5s',fid.read(5))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['rx_freq']=data_key
        
            if stop_key=='GI':
                data_tmp,=struct.unpack('16s',fid.read(16))
                data_key=data_tmp.decode('ascii','ignore').replace("\x00", " ").strip()
                info['GI']=data_key

            if stop_key=='R':
                break
            pos+=len_rec
    
        fid.seek(-4,1)

        data=np.zeros((info['n_sampler_y']+2,info['n_sampler_x']))
        for idx_z in range(info['n_sampler_x']):
            for idx_x in range(info['n_sampler_y']+2):
                pnt,=struct.unpack('h',fid.read(2))
                data[idx_x,idx_z]=pnt
        data=data[2:,:]
    return data,info

if __name__=='__main__':
    file_name='LZZ10001.dt'
    data,info=readIDS(file_name)
