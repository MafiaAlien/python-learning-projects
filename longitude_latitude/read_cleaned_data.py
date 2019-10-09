import pandas as pd
import os


def read_cleaned_data(path_clean):
	df_duplicated = pd.read_csv(path_clean, header=0)
	df_duplicated.dropna(axis=0, how='all', inplace=True)
	df_duplicated.drop(['Unnamed: 2'], axis=1, inplace=True)
	return df_duplicated


def merge_original_data(path_original):
	df_original = pd.DataFrame(columns=['mall_name', 'address', 'longitude', 'latitude'])
	for info in os.listdir(path_original):
		domain = os.path.abspath(path_original)
		info = os.path.join(domain, info)
		df_original.loc['city', :1] = info.split('\\')[-1]
		df_original = df_original.append(pd.read_csv(info, header=0), ignore_index=True, sort=False)
	df_original.dropna(axis=1, how='all', inplace=True)
	print(df_original, df_original.columns, df_original.index, end='\n')
	return df_original


def data_merge(df_original, df_duplicated):
	df = pd.concat([df_original, df_duplicated], axis=0, join='outer', sort=False, ignore_index=True)
	df.dropna(axis=1, how='all', inplace=True)
	df = df.drop_duplicates(subset=['mall_name'], keep=False, )
	df.to_csv('cleaned_addresses.csv', sep=',', index=False)
	print('merge finished')


if __name__ == '__main__':
	path_clean = r'D:\python\Wayz\longitude_latitude\duplicated_address.csv'
	path_original = r'D:\python\Wayz\longitude_latitude\commercial_data'
	df_duplicated = read_cleaned_data(path_clean)
	df_original = merge_original_data(path_original)
	data_merge(df_original, df_duplicated)
