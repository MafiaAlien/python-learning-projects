# coding=utf-8
from pyspark.sql.functions import *
from pyspark import SparkContext
from pyspark.sql import SQLContext
import csv
from pyspark.sql import dataframe
from pyspark.sql.types import *
import pandas as pd
from pyspark.sql import SparkSession, DataFrame

sc = SparkContext()
spark = SparkSession(sc)
sqlctx = SQLContext(sc)

path_res = r'D:\python\数据\logs\响应日志.txt'
path_request = r'D:\python\数据\logs\请求日志.txt'
path_supervise =r'D:\python\数据\logs\监测日志.txt'

# schema_res = [
# 	StructField('时间', StringType(), True),
# 	StructField('请求ID', StringType(), True),
# 	StructField('IP', IntegerType(), True),
# 	StructField('地域ID', IntegerType(), True),
# 	StructField('地域名称', StringType(), True),
# 	StructField('UserID', StringType(), True),
# 	StructField('广告位ID', IntegerType(), True),
# 	StructField('投放编号', StringType(), True),
# 	StructField('素材组ID', IntegerType(), True),
# 	StructField('素材ID', IntegerType(), True),
# 	StructField('referer', StringType(), True),
# 	StructField('UserAgent', StringType(), True),
# 	StructField('地理围栏ID', StringType(), True),
#
# ]

schema_super = [StructField('时间', StringType(), True),
				StructField('监测类型', StringType(), True),
				StructField('请求ID', StringType(), True),
				StructField('IP', StringType(), True),
				StructField('地域id', StringType(), True),
				StructField('地域名称', StringType(), True),
				StructField('UserID', StringType(), True),
				StructField('广告位ID', StringType(), True),
				StructField('投放编号', StringType(), True),
				StructField('素材ID', StringType(), True),
				StructField('referer', StringType(), True),
				StructField('userAgent', StringType(), True),
				StructField('价格', IntegerType(), True),
				]


def res_data_rearrange(path):
	"""响应日志格式重排"""
	lines = sqlctx.read.csv(path, header=False, inferSchema=True)
	# lines.show()
	# lines = lines.drop('_c0', '_c1')
	lines = lines.withColumn('_c0', split(lines['_c0'], r'\|\|'))\
		.withColumn('时间', col('_c0')[0]).withColumn('请求ID', col('_c0')[1])
	lines = lines.drop('_c0')
	lines = lines.withColumnRenamed('_c1', 'IP')\
		.withColumnRenamed('_c2', '地域ID')\
		.withColumnRenamed('_c3', '地域名称')\
		.withColumnRenamed('_c4', 'UserID')\
		.withColumnRenamed('_c5', '广告位ID')\
		.withColumnRenamed('_c6', '投放编号')\
		.withColumnRenamed('_c7', '素材组ID')\
		.withColumnRenamed('_c8', '素材ID')\
		.withColumnRenamed('_c10', 'referer')\
		.withColumnRenamed('_c11', 'UserAgent')
	return lines


def req_data_rearrange(path):
	"""请求日志格式重排"""
	lines = sqlctx.read.csv(path, header=False, inferSchema=True)
	# lines.show()
	# lines = lines.drop('_c0', '_c1')
	lines = lines.withColumnRenamed('_c0', '时间')\
		.withColumnRenamed('_c1', '请求ID')\
		.withColumnRenamed('_c2', '下游Token')\
		.withColumnRenamed('_c3', '接口版本号')\
		.withColumnRenamed('_c4', 'APP名称')\
		.withColumnRenamed('_c5', 'APP版本')\
		.withColumnRenamed('_c6', 'APP包名')\
		.withColumnRenamed('_c7', 'IP地址')\
		.withColumnRenamed('_c8', 'UserAgent')
	lines = lines.withColumnRenamed('_c9', '操作系统1:Android 2:iOS').withColumnRenamed('_c10',
																					'操作系统版本号').withColumnRenamed('_c11',
																												 '设备生产商')
	lines = lines.withColumnRenamed('_c12', '设备型号(UrlEncode)').withColumnRenamed('_c13', '屏幕分辨率宽').withColumnRenamed(
		'_c14', '屏幕分辨率高')
	lines = lines.withColumnRenamed('_c15', 'PPI').withColumnRenamed('_c16', 'Mac地址').withColumnRenamed('_c17',
																										'Mac地址MD5')
	lines = lines.withColumnRenamed('_c18', 'Mac地址去掉后MD5').withColumnRenamed('_c19', 'Idfa').withColumnRenamed('_c20',
																											   'Idfa Md5')
	lines = lines.withColumnRenamed('_c21', 'Openudid').withColumnRenamed('_c22', 'Openudid Md5').withColumnRenamed(
		'_c23', 'Imei')
	lines = lines.withColumnRenamed('_c24', 'Imei Md5').withColumnRenamed('_c25', 'Android Id').withColumnRenamed('_26',
																												  'Android Id Md5')
	lines = lines.withColumnRenamed('_c27', 'Android AD Id').withColumnRenamed('_c28',
																			   'ndroid AD Id Md5').withColumnRenamed(
		'_c29', '运营商').withColumnRenamed('_c30', '广告位ID')
	lines = lines.withColumnRenamed('_c31', '请求广告个数').withColumnRenamed('_c32', '广告位宽').withColumnRenamed('_33', '广告位高')
	lines = lines.withColumnRenamed('_c34', 'Gps定位类型').withColumnRenamed('_c35', '经度').withColumnRenamed('_c36',
																										 '纬度').withColumnRenamed(
		'_c37', '获取经纬度的时间戳(毫秒)')
	lines = lines.withColumnRenamed('_c38', 'crtg标签').withColumnRenamed('_c39', 'wifiList').withColumnRenamed('_c40',
																											  'appList')
	return lines


def super_rearrange(path):
	"""监测日志格式重排"""
	lines = sqlctx.read.csv(path, header=False, schema=StructType(schema_super))
	return lines


def write_ad_space_click_view(df_req, df_super):
	df_req_new = df_req.select('请求ID', '广告位ID')
	df_super_new = df_super.select('请求ID', '监测类型', 'UserID')
	df_req_new = df_req_new.groupby('请求ID', '广告位ID').count()
	df_super_new = df_super_new.groupby('请求ID', '监测类型')\
		.agg(count('请求ID').alias('数量'),	countDistinct('UserID').alias('UV数'))
	df_ad_space_click_view = df_req_new.join(df_super_new, '请求ID', 'inner')\
		.select(df_req_new['请求ID'], '监测类型', '数量', 'UV数')
	if df_ad_space_click_view:
		df_ad_space_click_view.show()
		df_ad_space_click_view.write.csv('ad_space_click_view', header=True, mode='ignore')
		print('ad_space_click_view文件已生成')
	else:
		print('ad_space_click_view文件生成失败')


def write_ad_space_count(df_req, df_res):
	df_req_new = df_req.select('请求ID', '广告位ID')
	df_res_new = df_res.select('请求ID', 'UserID')
	df_req_new = df_req_new.groupby('请求ID', '广告位ID').agg(count('请求ID').alias('请求数'),
														 countDistinct('请求ID').alias('请求UV'))
	df_res_new = df_res_new.groupby('请求ID').agg(count('请求ID').alias('响应数'),
												countDistinct('UserID').alias('响应UV'))
	df_ad_space_count = df_req_new.join(df_res_new, '请求ID', 'inner').select(df_req_new['请求ID'],
																			'广告位ID',
																			'请求数',
																			'请求UV',
																			'响应数',
																			'响应UV')
	if df_ad_space_count:
		df_ad_space_count.show()
		df_ad_space_count.write.csv('ad_space_count', header=True, mode='ignore')
		print('ad_space_count文件已生成')
	else:
		print('ad_space_count文件生成失败')

def write_app_click_view(df_super, df_req):
	df_req_new = df_req.select('请求ID', 'APP名称', 'APP包名')
	df_super_new = df_super.select('请求ID', '监测类型', 'UserID')
	df_req_new = df_req_new.groupby('请求ID', 'APP名称', 'APP包名').count()
	df_super_new = df_super_new.groupby('请求ID', '监测类型').agg(count('请求ID').alias('请求数'),
															countDistinct('UserID').alias('UV数'))
	df_app_click_view = df_req_new.join(df_super_new, '请求ID', 'inner').select(df_req_new['请求ID'],
	  									     'APP名称',
	  									     'APP包名',
											 '监测类型',
	 									     '请求数',
            								 'UV数', )
	if df_app_click_view:
		df_app_click_view.show()
		df_app_click_view.write.csv('app_click_view', header=True, mode='ignore')
		print('app_click_view文件已生成')
	else:
		print('app_click_view文件生成失败')


def write_app_count(df_req, df_res):
	df_req_new = df_req.select('请求ID', 'APP名称', 'APP包名')
	df_res_new = df_res.select('请求ID', 'UserID')
	df_req_new = df_req_new.groupby('请求ID', 'APP名称', 'APP包名').agg(count('请求ID').alias('请求数'),
																   countDistinct('请求ID').alias('请求UV'))
	df_res_new = df_res_new.groupby('请求ID').agg(count('UserID').alias('响应数'),
												countDistinct('UserID').alias('响应UV'))
	df_app_count = df_req_new.join(df_res_new,
								   '请求ID',
								   'inner',
								    ).select(df_req_new['请求ID'],
	  									     'APP名称',
	  									     'APP包名',
	 									     '请求数',
            								 '请求UV',
											 '响应数',
	 									     '响应UV')
	if df_app_count:
		df_app_count.show()
		df_app_count.write.csv('app_count', header=True, mode='ignore')
		print('app_count文件已生成')
	else:
		print('app_count文件生成失败')


def write_dispensing_number_click_view(df_super):
	df = df_super.select('投放编号', '广告位ID', '监测类型', 'UserID')
	df = df.groupby('投放编号', '广告位ID', '监测类型').agg(count('UserID').alias('数量'),
												countDistinct('UserID').alias('UV数'))
	if df:
		df.show()
		df.write.csv('dispensing_number_click_view', header=True, mode='ignore')
		print('Dispensing_click_view文件已生成')
	else:
		print('Dispensing_click_view文件生成失败')


def write_dispensing_number_count(df_res):
	"""编写响应数"""
	df = df_res.select('时间', '投放编号', '广告位ID', 'UserID')
	df = df.groupBy('投放编号', '广告位ID').agg(
		count('UserID').alias('响应数'),
		countDistinct('UserID').alias('响应UV数'))
	if df:
		df.show()
		df.write.csv('dispensing_number_count', header=True, mode='ignore')
		print('Dispensing_count文件已生成')
	else:
		print('Dispensing_count文件生成失败')


def write_material_click_view(df_super, df_res):
	df_super_new = df_super.select('请求ID', '素材ID')
	df_res_new = df_res.select('请求ID', 'UserID')
	df_super_new = df_super_new.groupby('请求ID', '素材ID').count()
	df_res_new = df_res_new.groupby('请求ID').agg(count('请求ID').alias('响应数'),
												countDistinct('UserID').alias('响应UV'))
	df_m_c_v = df_super_new.join(df_res_new, '请求ID', 'inner').select(df_super_new['请求ID'],
																	 '素材ID',
																	 '响应数',
																	 '响应UV')
	if df_m_c_v:
		df_m_c_v.show()
		df_m_c_v.write.csv('material_click_view', header=True, mode='ignore')
		print('material_click_view文件已生成')
	else:
		print('material_click_view文件生成失败')


def write_material_count(df_req, df_super):
	df_req_new = df_req.select('请求ID')
	df_super_new = df_super.select('请求ID', '素材ID', '监测类型', 'UserID')
	df_req_new = df_req_new.groupby('请求ID').count()
	df_super_new = df_super_new.groupby('请求ID', '素材ID','监测类型').agg(count('请求ID').alias('数量'),
														countDistinct('UserID').alias('UV数'))
	df_m_c = df_req_new.join(df_super_new, '请求ID', 'inner').select(df_req_new['请求ID'],
																   '素材ID',
																   '监测类型',
																   '数量',
																   'UV数')
	if df_m_c:
		df_m_c.show()
		df_m_c.write.csv('material_count', header=True, mode='ignore')
		print('material_count file established successfully')
	else:
		print('material_count file established unsuccessfully')


def write_token_app_click_view(df_req, df_super):
	df_req_new = df_req.select('请求ID', '下游Token', 'APP名称', '广告位ID')
	df_super_new = df_super.select('请求ID', '监测类型', 'UserID')
	df_req_new = df_req_new.groupby('请求ID', '下游Token', 'APP名称', '广告位ID').count()
	df_super_new = df_super_new.groupby('请求ID', '监测类型').agg(count('请求ID').alias('数量'),
															countDistinct('UserID').alias('UV数'))
	df_click_view_count = df_req_new.join(df_super_new, '请求ID', 'inner').select(df_req_new['请求ID'],
																				'下游Token',
																				'APP名称',
																				'广告位ID',
																				'数量',
																				"UV数")
	if df_click_view_count:
		df_click_view_count.show()
		df_click_view_count.write.csv('token_app_click_view', header=True, mode='ignore')
		print('token_app_click_view文件已生成')
	else:
		print('token_app_click_view文件生成失败')


def write_token_app_count(df_req, df_res, df_super):
	df_req_new = df_req.select('请求ID', '下游Token', 'APP名称', '广告位ID')
	df_res_new = df_res.select('请求ID', 'UserID')
	df_super_new = df_super.select('请求ID', '价格')
	df_req_new = df_req_new.groupby('请求ID', '下游Token', 'APP名称', '广告位ID').agg(count('请求ID').alias('请求数'),
																			 countDistinct('请求ID').alias('请求UV'))
	df_res_new = df_res_new.groupby('请求ID').agg(count('请求ID').alias('响应数'),
														  countDistinct('UserID').alias('响应UV'))
	df_token_count1_2 = df_req_new.join(df_res_new, '请求ID', 'inner').select(df_req_new['请求ID'],
																					     '下游Token',
																					     'APP名称',
																					     '广告位ID',
																					     '请求数',
																					     '请求UV',
																					     '响应数',
																					     '响应UV',
																					     )
	df_token_count = df_token_count1_2.join(df_super_new, '请求ID', 'inner').select(df_token_count1_2['请求ID'],
																					'下游Token',
																					'APP名称',
																					'广告位ID',
																					'请求数',
																					'请求UV',
																					'响应数',
																					'响应UV',
																				    '价格'
																				  )
	if df_token_count:
		df_token_count.show()
		df_token_count.write.csv('token_app_count', header=True, mode='ignore')
		print('token_app_count文件已生成')
	else:
		print('token_app_count文件生成失败')


def main():
	df_res = res_data_rearrange(path_res)
	df_req = req_data_rearrange(path_request)
	df_super = super_rearrange(path_supervise)
	write_dispensing_number_click_view(df_super)
	write_dispensing_number_count(df_res)
	write_ad_space_click_view(df_req, df_super)
	write_ad_space_count(df_req, df_res)
	write_app_click_view(df_super, df_req)
	write_app_count(df_req, df_res)
	write_material_click_view(df_super, df_res)
	write_material_count(df_req, df_super)
	write_token_app_click_view(df_req, df_super)  # 完成，待验证
	write_token_app_count(df_req, df_res, df_super)   # 已完成，有点问题，稍后修改


if __name__ == '__main__':
	main()
