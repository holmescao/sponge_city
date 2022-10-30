# 导入UI模块
from utils.ui.sponge_city import Ui_MainWindow  # 导入主窗口
from utils.ui_class.SimdateOptions import SimdateOptions
from utils.ui_class.GreenroofInput import GreenroofInput
from utils.ui_class.PermeablePavementInput import PermeablePavementInput
from utils.ui_class.Block import Block
from utils.ui_class.SpongeBlock import SpongeBlock
from utils.ui_class.RainGenerate import RainGenerate
from utils.ui_class.Export import Export
# 导入要执行的算法
from utils.algo.concave_herbaceous_field import ConcaveHerbaceousField
from utils.algo.permeable_pavement import PermeablePavement
from utils.algo.green_roof import GreenRoof
from utils.algo.bioretention_ponds import BioretentionPonds
from utils.algo.non_point_pollution import NonPointPollution
from utils.algo.sponge_block import NonPointControl
from utils.algo.green_roof_single import SingleGreenRoof
from utils.algo.permeable_pavement_single import SinglePermeablePavement
from utils.algo.sponge_district import SpongeDistrict
from utils.algo.general_functions import select_weather_file, select_district_file, export_experiment_results
# 导入其他库
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Application(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)

        self.setupUi(self)             # 创建界面

        """实例化-海绵单体模型"""
        # TODO：是不是要和斑块的模型合并？
        # 绿色屋顶模型
        self.SingleGreenRoof = SingleGreenRoof()
        self.SinglePermeablePavement = SinglePermeablePavement()

        """实例化-地块模型"""
        # 面源污染模型
        self.NonPointPollution = NonPointPollution()
        # 海绵模型
        self.NonPointControl = NonPointControl()
        self.BioretentionPonds = BioretentionPonds()
        self.GreenRoof = GreenRoof()
        self.PermeablePavement = PermeablePavement()
        self.ConcaveHerbaceousField = ConcaveHerbaceousField()

        """实例化-城区模型"""
        self.SpongeDistrict = SpongeDistrict()

        """实例化-输入界面"""
        self.export_Dialog = Export(self)
        self.block_Dialog = Block(self)
        self.sponge_block_Dialog = SpongeBlock(self)
        self.sim_datetime_Dialog = SimdateOptions(self)
        self.rain_generate_Dialog = RainGenerate(self)
        self.green_roof_Dialog = GreenroofInput(self)
        self.permeable_pavement_Dialog = PermeablePavementInput(self)

        """输入/输出-主窗口"""
        self.action_weather_file_load.triggered.connect(  # 导入天气文件
            lambda: select_weather_file(self))
        self.action_district_file_load.triggered.connect(  # 导入城区文件
            lambda: select_district_file(self))
        self.action_expr_res_export.triggered.connect(  # 导出实验结果
            lambda: self.export_Dialog.open_export_Dialog(self,))  # TODO：输出的文件只有4个污染物

        """选择-海绵单体"""
        self.listView.clicked.connect(self.select_haimian)  # 点击选择海绵体，弹窗选择参数

        """选择-工具栏"""
        # 仿真起止日期和步长
        self.start_dt_str = ""
        self.end_dt_str = ""
        self.time_step = ""
        self.ADP = -1
        self.actionDates.triggered.connect(
            lambda: self.sim_datetime_Dialog.open_sim_datetime_dialog(self,))
        # 面源斑块
        self.action_Block.triggered.connect(
            lambda: self.block_Dialog.open_block_dialog(self.NonPointPollution,))
        # 海绵地块
        self.action_SpongeBlock.triggered.connect(
            lambda: self.sponge_block_Dialog.open_sponge_block_dialog(self.block_Dialog, self))
        # 雨型生成
        self.action_rain_generate.triggered.connect(
            lambda: self.rain_generate_Dialog.open_rain_generate_dialog(self,))

        """运行-工具栏"""
        self.green_roof_single_sim_flag = False
        self.permeable_pavement_single_sim_flag = False
        self.block_sim_flag = False
        self.sponge_block_sim_flag = False
        self.sponge_district_sim_flag = False

        # TODO: 把仿真日期参数在每个仿真函数里面的最开头添加
        # 绿色屋顶仿真
        self.action_sim_green_roof.triggered.connect(
            lambda: self.SingleGreenRoof.green_roof_sim(self))
        # 渗透铺装仿真
        self.action_sim_permeablepavement.triggered.connect(
            lambda: self.SinglePermeablePavement.permeable_pavement_sim(self))
        # self.action_sim_and_val_green_roof.triggered.connect(
        #     lambda: self.SingleGreenRoof.green_roof_sim_and_val(self))  # 仿真&验证 TODO：可以去除
        # 面源斑块仿真
        self.action_sim_block.triggered.connect(
            lambda: self.NonPointPollution.block_sim(self, self.rain_generate_Dialog, self.block_Dialog))
        # 海绵地块仿真
        self.action_sim_sponge_block.triggered.connect(
            lambda: self.NonPointControl.sponge_block_sim(self, self.NonPointPollution,
                                                          self.GreenRoof, self.PermeablePavement, self.BioretentionPonds, self.ConcaveHerbaceousField,
                                                          self.rain_generate_Dialog, self.block_Dialog, self.sponge_block_Dialog))

        # 海绵城区仿真
        self.district_file_path = "district.xlsx"  # TODO:临时测试，之后要删掉
        self.action_sim_district.triggered.connect(
            lambda: self.SpongeDistrict.sponge_district_sim(self, self.NonPointPollution,
                                                            self.GreenRoof, self.PermeablePavement, self.BioretentionPonds, self.ConcaveHerbaceousField,
                                                            self.rain_generate_Dialog, self.block_Dialog, self.sponge_block_Dialog))

    def select_haimian(self, item):
        # TODO：其他海绵的单体模型
        # ["绿色屋顶","渗透铺装", "下凹式绿地", "生物滞留池"]
        if self.haimain_list[item.row()] == "绿色屋顶":
            self.green_roof_Dialog.open_green_roof_Dialog(
                self.green_roof_Dialog, self.SingleGreenRoof)
        elif self.haimain_list[item.row()] == "渗透铺装":
            self.permeable_pavement_Dialog.open_permeable_pavement_Dialog(
                self.permeable_pavement_Dialog, self.SinglePermeablePavement)
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)                    # 创建应用程序对象
    mainWindow = Application()                      # 实例化界面
    mainWindow.show()                               # 窗口显示
    sys.exit(app.exec_())                           # 主循环结束
