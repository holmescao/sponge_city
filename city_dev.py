"""
1. 用户在UI界面选择excel文件路径
2. 加载excel文件内容
3. 将excel文件内容赋值给相应模块的相关参数
4. 挨个模拟各个斑块的径流、污染
5. 挨个模拟各个海绵地块的径流、污染
6. 结构化各个地块模拟结果
7. 根据径流时间序列，迭代受纳河流的径流、污染变化情况
8. 可视化
9. 结果保存
"""
import pandas as pd


def load_sponge_district_file(file_path):
    io = pd.io.excel.ExcelFile(file_path)
    block_river_map = pd.read_excel(io, sheet_name='地块-河流').values
    rivers_map = pd.read_excel(io, sheet_name='主干-支流').values
    block_map = pd.read_excel(io, sheet_name='地块').values
    io.close()

    return block_map, rivers_map, block_river_map


def assign_params_values():
    return


def district_sim():
    """挨个模拟地块（斑块、海绵）"""

    """结果结构化"""
    return


def river_sim():
    """河流水文、水质模拟"""
    return


sponge_city_building_file_path = 'district.xlsx'

block_map, rivers_map, block_river_map = load_sponge_district_file(
    sponge_city_building_file_path)
