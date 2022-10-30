import numpy as np
import os


class ConcaveHerbaceousField:
    def __init__(self,
                 underlyingsurface_loss_list=[],
                 underlyingsurface_infil_list=[],
                 weather_file_path="") -> None:
        """参数初始化"""

        # 仿真起止时间，及时间步长
        self.start_dt_str = "2022-08-21 00:00"
        self.end_dt_str = "2022-08-21 06:00"
        self.Tstep = 1/60               # time step (hr),min
        self.ADP = -1  # 雨前干旱时长（day）

        self.underlyingsurface_loss_list = underlyingsurface_loss_list
        self.underlyingsurface_infil_list = underlyingsurface_infil_list

        self.rainfall = None  # 降雨量，mm/hr
        # 设置循环长度
        self.LoopCount = 0
        # 文件路径
        self.weather_file_path = weather_file_path

    @property
    def pack_params(self):
        green_roof_params_dict = {
            "蓄水层": {
                "蓄水层水深": self.d3_0,
                "蓄水层深度": self.D3,
                "蓄水层最小可出流深度": self.D3D,
                "砾石层孔隙率": self.phi3,
                "孔流系数": self.C3D,
                "孔流指数": self.eta3D,
            },
            "土壤层": {
                "土层含水量": self.xita2_0,
                "基质层深度": self.D2,
                "田间持水量": self.xitaFC,
                "凋萎点": self.xitaWP,
                "土壤层孔隙率": self.phi2,
                "临界含水量": self.xitacb,
                "饱和导水率": self.Ksat,
                "衰减常数": self.HCO,
                "吸力水头": self.psi2,
            },
            "表层": {
                "溢流层深度": self.D1,
                "空隙率": self.phi1,
            }
        }

        #  green_roof_params_dict = {
        #     "蓄水层":{
        #         "蓄水层水深":self.GreenRoof.d3_0,
        #         "蓄水层深度":self.GreenRoof.D3,
        #         "蓄水层最小可出流深度":self.GreenRoof.D3D,
        #         "砾石层孔隙率":self.GreenRoof.phi3,
        #         "孔流系数":self.GreenRoof.C3D,
        #         "孔流指数":self.GreenRoof.eta3D,
        #     },
        #     "土壤层":{
        #         "土层含水量":self.GreenRoof.xita2_0,
        #         "基质层深度":self.GreenRoof.D2,
        #         "田间持水量":self.GreenRoof.xitaFC,
        #         "凋萎点":self.GreenRoof.xitaWP,
        #         "土壤层孔隙率":self.GreenRoof.phi2,
        #         "临界含水量":self.GreenRoof.xitacb,
        #         "饱和导水率":self.GreenRoof.Ksat,
        #         "衰减常数":self.GreenRoof.HCO,
        #         "吸力水头":self.GreenRoof.psi2,
        #     },
        #     "表层":{
        #         "溢流层深度":self.GreenRoof.D1,
        #         "空隙率":self.GreenRoof.phi1,
        #     }
        # }

        return green_roof_params_dict

    @property
    def get_weather_data(self):
        # 输入计算蒸散发所需的气象数据
        data = np.loadtxt(self.weather_file_path)
        self.rainfall = data[:]  # 降雨量，mm/hr

        # 设置循环长度
        self.LoopCount = len(data)

    # @property
    def sim(self, runoff, pollution):
        # self.get_weather_data

        sponge_runoff = np.zeros_like(runoff)

        pp_metric = list(pollution.keys())
        sponge_pollution = dict(zip(pp_metric, range(len(pp_metric))))
        reduction = 0.3
        sponge_runoff[:, 0] = runoff[:, 0] * (1-reduction)

        for name, val in pollution.items():
            sponge_pollution[name] = val * (1-reduction)

        return sponge_runoff, sponge_pollution
