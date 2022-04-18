import os
import pandas as pd
from core.client.wayz_client.wayz_client import WayzClient, WayzClientError
import json
import datetime


class HonorData:
    def __init__(self, filepath):
        self.df_template = pd.DataFrame()
        self.filepath = filepath
        self.writer = pd.ExcelWriter(f'荣耀数据{datetime.date.today()}.xlsx')
        self._res = {}


    def _load_excel_data(self):
        df = pd.read_excel(self.filepath)
        return df

    def _parse_df(self):
        df = self._load_excel_data()
        params_list = {}
        for i in range(len(df)):
            include_by_geofences = {}
            geofence = {}
            geofences = []
            include_by_geofences["op_relation"] = 1
            if df['地理围栏类型'].iloc[i] == '多边形':
                geofence["geofence_type"] = 2
                geofence["polygon"] = f'{df["多边形(地理围栏为多边形时填写)"].iloc[i]}'
            else:
                geofence["geofence_type"] = 1
                geofence.update(
                        radius=str(df["半径(地理围栏为圆时填写)"].iloc[i]),
                        longitude=str(df["经纬度(地理围栏为圆时填写)"].iloc[i].split(",")[0]),
                        latitude=str(df["经纬度(地理围栏为圆时填写)"].iloc[i].split(",")[1]),
                    )
            if df['人群类型'].iloc[i] == '到访':
                geofence.update(
                    filter_type=0,
                    start_date=str(df['开始时间'].iloc[i]),
                )
                if df['筛选白天/晚上(人群类型为到访时才填写)'].iloc[i] == '全部':
                    geofence.update(day_night=0)
                elif df['筛选白天/晚上(人群类型为到访时才填写)'].iloc[i] == '白天':
                    geofence.update(day_night=1)
                else:
                    geofence.update(day_night=2)
                if df['工作日、周末(人群类型为到访时才填写)'].iloc[i] == '全部':
                    geofence.update(workday_weekend=0)
                elif df['工作日、周末(人群类型为到访时才填写)'].iloc[i] == '工作日':
                    geofence.update(workday_weekend=1)
                else:
                    geofence.update(workday_weekend=2)

            elif df['人群类型'].iloc[i] == '工作':
                geofence["filter_type"] = 2
            elif df['人群类型'].iloc[i] == '居住':
                geofence["filter_type"] = 1
            else:
                geofence["filter_type"] = 4

            if df['人群类型'].iloc[i] == '到访':
                geofences.append(geofence)
                include_by_geofences["geofences"] = geofences
                params_list[df['人群包名称'].iloc[i]] = {}
                params_list[df['人群包名称'].iloc[i]]['城市code'] = df["城市code"].iloc[i]
                params_list[df['人群包名称'].iloc[i]]["req_params"] = dict(
                    month=str(df["月份"].iloc[i]),
                    include_by_geofences=include_by_geofences)
            else:
                geofences.append(geofence)
                include_by_geofences["geofences"] = geofences
                params_list[df['人群包名称'].iloc[i]] = {}
                params_list[df['人群包名称'].iloc[i]]['城市code'] = df["城市code"].iloc[i]
                params_list[df['人群包名称'].iloc[i]]["req_params"] = dict(include_by_geofences=include_by_geofences)

        # print(params_list)
        return params_list

    def _req_tag(self, params):
        for k, v in params.items():
            try:
                res = WayzClient().crowd_tag(v['req_params'])
                self._res[k] = dict(req=v['req_params'], citycode=str(v['城市code']), res=res)
                print(f'{k}:请求参数：{v["req_params"]}, 返回结果：{res}, citycode:{v["城市code"]}')
            except WayzClientError as e:
                print(f'{k} fail. detail: {str(e)}')

    def _req_count(self, params):
        df_res = pd.DataFrame()
        for k, v in params.items():
            try:
                res = WayzClient().crowd_count(v['req_params'])
                self._res[k] = dict(req=v['req_params'], citycode=str(v['城市code']), res=res)
                print(f'{k}:请求参数：{v["req_params"]}, 返回结果：{res}, citycode:{v["城市code"]}')
                df_res = df_res.append(dict(
                    CrowdPackName=k,
                    Count=res['data'],
                ), ignore_index=True)
            except WayzClientError as e:
                print(f'{k} fail. detail: {str(e)}')

        self._save_to_excel(df_res)

    def _save_to_json(self):
        save_path = r'D:\WAYZ\wayz_midend_data_run\core\other_scripts\honor'
        result_file = os.path.join(save_path, f'荣耀_{datetime.date.today()}_res.json')
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump(self._res, f, ensure_ascii=False)
            print('finished')

    def _save_to_excel(self, df):
        df.to_excel(self.writer, index=False, header=True)
        self.writer.save()

    def main_tag(self):
        req_params = self._parse_df()
        self._req_tag(req_params)
        self._save_to_json()

    def main_cnt(self):
        req_params = self._parse_df()
        self._req_count(req_params)
        self._save_to_json()



if __name__ == "__main__":
    h = HonorData(r'D:\WAYZ\wayz_midend_data_run\core\data\19城1000m范围-到访.xlsx')
    h.main_cnt()


