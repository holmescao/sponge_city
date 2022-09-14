## 面源污染负荷估算主程序
import os
from datetime import datetime
import pandas as pd
import xlrd
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QMessageBox

class Dict(dict):

    def __getattr__(self, key):
        return self.get(key)

    def __setattr__(self, key, value):
        self[key] = value

class NonPointPollution:
    def __init__(self) -> None:
        pass
    
    def change_landuse_params(self,block_Dialog):
        # TODO: 根据 landuse_type 改变显示的参数值
        landuse_type = block_Dialog.comboBox_landuse.currentText()
        
        block_Dialog.doubleSpinBox_Bmax_SS.setValue(999)
        
        return block_Dialog
    
    def change_underlyingsurface_params(self,block_Dialog):
        # TODO: 根据 underlyingsurface_type 改变显示的参数值
        underlyingsurface_type = block_Dialog.comboBox_underlyingsurface.currentText()
        
        block_Dialog.doubleSpinBox_Bmax_SS.setValue(999)
        
        return block_Dialog
        
    def update_params(self, block_Dialog):
        if block_Dialog.comboBox_landuse.currentText() == "请选择":
            QMessageBox.critical(
            block_Dialog,
            '错误',
            "请选择土地利用类型！")
            return 
        if block_Dialog.comboBox_underlyingsurface.currentText() == "请选择":
            QMessageBox.critical(
            block_Dialog,
            '错误',
            "请选择下垫面类型！")
            return 
        
        # block_Dialog.doubleSpinBox_Bmax_SS.setValue(999)
        return block_Dialog
    
    def reset_params(self, block_Dialog, temp_block_params):
        
        # 重置土地利用类型和下垫面参数
        block_Dialog.comboBox_landuse.setCurrentText(temp_block_params.landuse)
        block_Dialog.comboBox_underlyingsurface.setCurrentText(temp_block_params.underlyingsurface)
        
        # TODO:把 temp_block_Dialog 的所有参数赋给 block_Dialog
        block_Dialog.doubleSpinBox_Bmax_SS.setValue(temp_block_params.Bmax_SS)
        
        return block_Dialog
    
    def Temp_assign_params(self, block_Dialog):
        # TODO：添加参数
        temp_block_params = dict()
        temp_block_params["landuse"] = block_Dialog.comboBox_landuse.currentText()
        temp_block_params["underlyingsurface"] = block_Dialog.comboBox_underlyingsurface.currentText()
        temp_block_params["Bmax_SS"] = block_Dialog.doubleSpinBox_Bmax_SS.value()
        
        return Dict(temp_block_params)
        
    
def get_month(begin,end):
    begin_year,end_year=begin.year,end.year
    begin_month,end_month=begin.month,end.month
    if begin_year==end_year:
        months=end_month-begin_month
    else:
        months=(end_year-begin_year)*12+end_month-begin_month
    return months + 1
