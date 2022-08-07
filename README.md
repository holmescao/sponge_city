# 海绵城市模型
## 程序整体介绍
- `main_greenroof.py`: 软件主函数
- `sponge_city.py`: GUI界面函数（由.ui文件生成）
- `sponge_city.ui`: GUI界面设计文件
- `utils`
    + `green_roof.py`: 绿色屋顶模型
- `ref`: 原始模型

## 数据介绍
输入数据存在`data`目录下
- `green_roof`
    + `meteor1min20210525_0628.txt`: 绿色屋顶对应的气象数据
    + `obsnumberoutflow20210525_0628.txt`: 绿色屋顶出流实测数据

## 环境安装
```python
conda create -n SC python=3.7
conda activate SC
pip install -r requirements.txt
```
## 执行
在`code_root`下，运行
```python
python main_greenroof.py
```
即可打开GUI

**\* 详细的说明见软件使用说明文档。**