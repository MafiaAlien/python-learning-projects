import pandas as pd
from math import sin, cos, asin, radians, sqrt


def file_load(path):
	"""文件载入"""
	df = pd.read_csv(path, header=0, sep=",")
	return df


def distance_calculate(lon1, lat1, lon2, lat2):
	"""计算经纬度距离
	:param lon1, lon2 经度
	:param lat1, lat2 纬度"""
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
	c = 2 * asin(sqrt(a))
	r = 6371  # 地球平均半径， unit 为km
	result = c * r * 1000  # unit 为m
	return result


def delete_duplication(df, file_name):
	"""创建重复地址的dataframe"""
	df_duplicated = pd.DataFrame(columns=['mall_name1', 'address1', 'lon1', 'lat1',
										  'mall_name2', 'address2', 'lon2', 'lat2',
										  'distance'
										  ])
	for i in df.index:  # index1，
		for j in df.index:  # index2 用index1去组合index2计算经纬度距离
			if j <= i:
				continue
			lon1 = df.loc[i, 'longitude']
			lat1 = df.loc[i, 'latitude ']
			lon2 = df.loc[j, 'longitude']
			lat2 = df.loc[j, 'latitude ']
			distance = distance_calculate(lon1, lat1, lon2, lat2)
			if distance < 100:  # 预设同一商场最小可能的距离值，小于该距离则判断为同一location
				df_duplicated = df_duplicated.append({
					'mall_name1': df.loc[i, 'mall_name'],
					'mall_name2': df.loc[j, 'mall_name'],
					'address1': df.loc[i, 'address'],
					'address2': df.loc[j, 'address'],
					'lon1': lon1,
					'lat1': lat1,
					'lon2': lon2,
					'lat2': lat2,
					'distance': distance}, ignore_index=True)
	df_duplicated.to_csv(file_name + " duplication.csv", sep=',')
	print(file_name + ' duplication has been generated')


if __name__ == "__main__":
	pathes = [r'D:\python\Wayz\longitude_latitude\commercial_data\beijing.csv',
			  r'D:\python\Wayz\longitude_latitude\commercial_data\changsha.csv',
			  r'D:\python\Wayz\longitude_latitude\commercial_data\chengdu.csv',
			  r'D:\python\Wayz\longitude_latitude\commercial_data\chongqing.csv',
			  r'D:\python\Wayz\longitude_latitude\commercial_data\dongguan.csv',
			  r'D:\python\Wayz\longitude_latitude\commercial_data\guangzhou.csv',
			  r'D:\python\Wayz\longitude_latitude\commercial_data\hangzhou.csv',
			  r'D:\python\Wayz\longitude_latitude\commercial_data\kunming.csv',
			  r'D:\python\Wayz\longitude_latitude\commercial_data\nanjing.csv',
			  r'D:\python\Wayz\longitude_latitude\commercial_data\ningbo.csv',
			  r'D:\python\Wayz\longitude_latitude\commercial_data\qingdao.csv',
			  r'D:\python\Wayz\longitude_latitude\commercial_data\shanghai.csv',
			  r'D:\python\Wayz\longitude_latitude\commercial_data\shenyang.csv',
			  r'D:\python\Wayz\longitude_latitude\commercial_data\shenzhen.csv',
			  r'D:\python\Wayz\longitude_latitude\commercial_data\suzhou.csv',
			  r'D:\python\Wayz\longitude_latitude\commercial_data\tianjin.csv',
			  r'D:\python\Wayz\longitude_latitude\commercial_data\wuhan.csv',
			  r'D:\python\Wayz\longitude_latitude\commercial_data\xi_an.csv',
			  r'D:\python\Wayz\longitude_latitude\commercial_data\zhengzhou.csv',

			  ]
	for path in pathes:
		file_name = path.split('\\')[-1]
		df = file_load(path)
		delete_duplication(df, file_name)

	print('finished')
