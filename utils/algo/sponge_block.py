import numpy as np
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def sponge_block_pollution(area,sponge_tpye_area_map,**kwargs):
    first_type = list(kwargs.keys())[0]
    pollution_metric = list(kwargs[first_type].keys())
    series_step = kwargs[first_type][pollution_metric[0]].shape[0]
    pollution = dict(zip(pollution_metric,np.zeros(series_step)))
    
    for key, val in kwargs.items():
        w = sponge_tpye_area_map[key] / area # 计算权重
        
        for p in pollution.keys():
            pollution[p] += w * val[p]
 
    return pollution

def sponge_block_runoff(area,sponge_tpye_area_map,**kwargs):
    first_type = list(kwargs.keys())[0]
    series_step = kwargs[first_type].shape[0]
    overall_runoff = np.zeros(series_step)
    
    for key, val in kwargs.items():
        w = sponge_tpye_area_map[key] / area # 计算权重
        overall_runoff = overall_runoff + w * val[:,0]
 
    return overall_runoff

def available(tableWidget,row,col_range):
    for col in col_range:
        item0 = tableWidget.item(row,col)
        # item0.setText("是")
        item0.setBackground(QBrush(QColor(255,255,255)))
        item0.setFlags(QtCore.Qt.ItemFlag(63))
        tableWidget.setItem(row, 0, item0)

    return tableWidget

def forbidden(tableWidget,row,col_range,zero_flag=True):
    """禁止对表格两列的编辑，并赋默认值

    Args:
        tableWidget (_type_): _description_
        row (_type_): _description_

    Returns:
        _type_: _description_
    """
    for col in col_range:
        item0 = tableWidget.item(row,col)
        if zero_flag:
            item0.setText("0")
        # item0.setBackground(QBrush(QColor(128,128,128)))
        item0.setFlags(QtCore.Qt.ItemFlag(1))
        item0.setFlags(QtCore.Qt.ItemIsEditable)
    
    return tableWidget