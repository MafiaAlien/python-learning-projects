from functools import partial
from pyspark.sql.functions import *
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *

sc = SparkContext()
sqlctx = SQLContext(sc)

path_res = r'D:\python\Wayz\logs_to_csv\lba_logs\lba-new\20190715\response\00\201907150000_prod-LBA-delivery-tomcat-01_0.gz'
path_request = r'D:\python\Wayz\logs_to_csv\lba_logs\lba-new\20190715\request\00\201907150000_prod-LBA-delivery-tomcat-01_0.gz'
path_supervise = r'D:\python\Wayz\logs_to_csv\lba_logs\lba-new\20190715\event\00\201907150000_prod-LBA-collector-tomcat-01_0.gz'


def clean_line(line, _type):
    item_count = line.count(',')
    if _type == "event" and item_count == 13:
        line = line.replace(',', '|', 4)
        line = line.replace('|', ',', 3)
    elif _type == "response" and item_count == 12:
        line = line.replace(',', '`|`', 2)
        line = line.replace('`|`', ',', 1)
    elif _type == "request" and item_count == 41:
        line = line.replace(',', '|', 8)
        line = line.replace('|', ',', 7)
    return line.strip('"}').split('{"message":"')[-1]


def split_return_datetime_request_id(sub_string):
    row = sub_string.split('||')
    return row if len(row) > 1 else ["", ""]


udf_event_line_check = udf(partial(clean_line, _type="event"), StringType())
udf_request_line_check = udf(partial(clean_line, _type="request"), StringType())
udf_response_line_check = udf(partial(clean_line, _type="response"),
                              StringType())
udf_split_return_datetime_request_id = udf(split_return_datetime_request_id,
                                           ArrayType(StringType()))


def res_data_rearrange(path):
    """响应日志格式重排"""
    lines = sqlctx.read.text(path)
    lines = lines.withColumn('value', udf_response_line_check(lines.value))
    lines = lines.withColumn("value", split(lines['value'], r',')) \
        .withColumn("时间",
                    udf_split_return_datetime_request_id(col('value')[0])[0]) \
        .withColumn("请求ID",
                    udf_split_return_datetime_request_id(col('value')[0])[1]) \
        .withColumn("IP", col('value')[1]) \
        .withColumn("地域ID", col('value')[2]) \
        .withColumn("地域名称", col('value')[3]) \
        .withColumn("UserID", col('value')[4]) \
        .withColumn("广告位ID", col('value')[5]) \
        .withColumn("投放编号", col('value')[6]) \
        .withColumn("素材组ID", col('value')[7]) \
        .withColumn("素材ID", col('value')[8]) \
        .withColumn("referer", col('value')[9]) \
        .withColumn("UserAgent", col('value')[10])

    lines = lines.drop('value')
    return lines


def req_data_rearrange(path):
    """请求日志格式重排"""
    lines = sqlctx.read.text(path)
    lines = lines.withColumn('value', udf_request_line_check(lines.value))
    lines = lines.withColumn("value", split(lines['value'], r',')) \
        .withColumn("时间", col('value')[0]) \
        .withColumn("请求ID", col('value')[1]) \
        .withColumn("下游Token", col('value')[2]) \
        .withColumn("接口版本号", col('value')[3]) \
        .withColumn("APP名称", col('value')[4]) \
        .withColumn("APP版本", col('value')[5]) \
        .withColumn("APP包名", col('value')[6]) \
        .withColumn("IP地址", col('value')[7]) \
        .withColumn("UserAgent", col('value')[8]) \
        .withColumn("操作系统1:Android 2:iOS", col('value')[9]) \
        .withColumn("操作系统版本号", col('value')[10]) \
        .withColumn("Mac地址", col('value')[16]) \
        .withColumn("Imei", col('value')[23]) \
        .withColumn("广告位ID", col('value')[30]) \
        .withColumn("请求广告个数", col('value')[31])

    lines = lines.drop('value')
    return lines


def super_rearrange(path):
    """监测日志格式重排"""
    lines = sqlctx.read.text(path)
    lines = lines.withColumn('value', udf_event_line_check(lines.value))
    lines = lines.withColumn("value", split(lines['value'], r',')) \
        .withColumn("时间", col('value')[0]) \
        .withColumn("监测类型", col('value')[1]) \
        .withColumn("请求ID", col('value')[2]) \
        .withColumn("IP", col('value')[3]) \
        .withColumn("地域ID", col('value')[4]) \
        .withColumn("地域名称", col('value')[5]) \
        .withColumn("UserID", col('value')[6]) \
        .withColumn("广告位ID", col('value')[7]) \
        .withColumn("投放编号", col('value')[8]) \
        .withColumn("素材ID", col('value')[9]) \
        .withColumn("referer", col('value')[10]) \
        .withColumn("userAgent", col('value')[11]) \
        .withColumn("价格", col('value')[12])

    lines = lines.drop('value')
    return lines


def write_ad_space_click_view(df_req, df_super):
    df_req_new = df_req.select('请求ID', '广告位ID')
    df_super_new = df_super.select('请求ID', '监测类型', 'UserID')
    df_req_new = df_req_new.groupby('请求ID', '广告位ID').count()
    df_super_new = df_super_new.groupby('请求ID', '监测类型').agg(
        count('请求ID').alias('数量'),
        countDistinct('UserID').alias('UV数'))
    df_ad_space_click_view = df_req_new.join(
        df_super_new, df_req_new['请求ID'] == df_super_new['请求ID'], how='inner').select(
        df_req_new['请求ID'], '监测类型', '数量', 'UV数')
    if df_ad_space_click_view:
        df_ad_space_click_view.show()
        df_ad_space_click_view.coalesce(1).write.csv('ad_space_click_view',
                                                     header=True,
                                                     mode='ignore')

        print('ad_space_click_view文件已生成')
    else:
        print('ad_space_click_view文件生成失败')


def write_ad_space_count(df_req, df_res):
    df_req_new = df_req.select('请求ID', '广告位ID')
    df_res_new = df_res.select('请求ID', 'UserID')
    df_req_new = df_req_new.groupby('请求ID', '广告位ID').agg(
        count('请求ID').alias('请求数'),
        countDistinct('请求ID').alias('请求UV'))
    df_res_new = df_res_new.groupby('请求ID').agg(
        count('请求ID').alias('响应数'), countDistinct('UserID').alias('响应UV'))

    df_ad_space_count = df_req_new.join(df_res_new, '请求ID', 'inner'
                                        ).select(
        df_req_new['广告位ID'], '广告位ID', '请求数', '请求UV', '响应数', '响应UV')

    if df_ad_space_count:
        df_ad_space_count.show()
        df_ad_space_count.coalesce(1).write.csv('ad_space_count', header=True,
                                                mode='ignore')
        print('ad_space_count文件已生成')
    else:
        print('ad_space_count文件生成失败')


def write_app_click_view(df_super, df_req):
    df_req_new = df_req.select('请求ID', 'APP名称', 'APP包名')
    df_super_new = df_super.select('请求ID', '监测类型', 'UserID')
    df_req_new = df_req_new.groupby('请求ID', 'APP名称', 'APP包名').count()
    df_super_new = df_super_new.groupby('请求ID', '监测类型').agg(
        count('请求ID').alias('请求数'),
        countDistinct('UserID').alias('UV数'))
    df_app_click_view = df_req_new.join(df_super_new, '请求ID', 'inner'
                                        ).select(
        df_req_new['广告位ID'], 'APP名称', 'APP包名', '监测类型', '请求数', 'UV数')

    if df_app_click_view:
        df_app_click_view.show()
        df_app_click_view.coalesce(1).write.csv('app_click_view', header=True,
                                                mode='ignore')
        print('app_click_view文件已生成')
    else:
        print('app_click_view文件生成失败')


def write_app_count(df_req, df_res):
    df_req_new = df_req.select('请求ID', 'APP名称', 'APP包名')
    df_res_new = df_res.select('请求ID', 'UserID')
    df_req_new = df_req_new.groupby('请求ID', 'APP名称', 'APP包名').agg(
        count('请求ID').alias('请求数'),
        countDistinct('请求ID').alias('请求UV'))
    df_res_new = df_res_new.groupby('请求ID').agg(
        count('UserID').alias('响应数'), countDistinct('UserID').alias('响应UV'))

    df_app_count = df_req_new.join(df_res_new, '请求ID', 'inner',
                                   ).select(
        df_req_new['广告位ID'], 'APP名称', 'APP包名', '请求数', '请求UV', '响应数',
        '响应UV')

    if df_app_count:
        df_app_count.show()
        df_app_count.coalesce(1).write.csv('app_count', header=True,
                                           mode='ignore')
        print('app_count文件已生成')
    else:
        print('app_count文件生成失败')


def write_dispensing_number_click_view(df_super):
    df = df_super.select('投放编号', '广告位ID', '监测类型', 'UserID')
    df_total = df.agg(
        count('UserID').alias('响应数'),
        countDistinct('UserID').alias('响应UV数'))
    df_total.show()

    df = df.groupby('投放编号', '广告位ID', '监测类型').agg(
        count('UserID').alias('数量'), countDistinct('UserID').alias('UV数'))

    if df:
        df.show()
        df.coalesce(1).write.csv('dispensing_number_click_view', header=True,
                                 mode='ignore')
        print('Dispensing_click_view文件已生成')
    else:
        print('Dispensing_click_view文件生成失败')


def write_dispensing_number_count(df_res):
    """编写响应数"""
    df = df_res.select('时间', '投放编号', '广告位ID', 'UserID')
    df_total = df.agg(
        count('UserID').alias('响应数'),
        countDistinct('UserID').alias('响应UV数'))
    df_total.show()

    df = df.groupBy('投放编号', '广告位ID').agg(
        count('UserID').alias('响应数'),
        countDistinct('UserID').alias('响应UV数'))
    if df:
        df.show()
        df.coalesce(1).write.csv('dispensing_number_count', header=True,
                                 mode='ignore')
        print('Dispensing_count文件已生成')
    else:
        print('Dispensing_count文件生成失败')


def write_material_click_view(df_super, df_res):
    df_super_new = df_super.select('请求ID', '素材ID')
    df_res_new = df_res.select('请求ID', 'UserID')
    df_super_new = df_super_new.groupby('请求ID', '素材ID').count()
    df_res_new = df_res_new.groupby('请求ID').agg(count('请求ID').alias('响应数'),
                                                countDistinct('UserID').alias(
                                                    '响应UV'))
    df_m_c_v = df_super_new.join(df_res_new, '请求ID', 'inner'
                                 ).select(
        df_super_new['请求ID'], '素材ID', '响应数', '响应UV')

    if df_m_c_v:
        df_m_c_v.show()
        df_m_c_v.coalesce(1).write.csv('material_click_view', header=True,
                                       mode='ignore')
        print('material_click_view文件已生成')
    else:
        print('material_click_view文件生成失败')


def write_material_count(df_req, df_super):
    df_req_new = df_req.select('请求ID')
    df_super_new = df_super.select('请求ID', '素材ID', '监测类型', 'UserID')
    df_req_new = df_req_new.groupby('请求ID').count()
    df_super_new = df_super_new.groupby('请求ID', '素材ID', '监测类型').agg(
        count('请求ID').alias('数量'),
        countDistinct('UserID').alias('UV数'))
    df_m_c = df_req_new.join(df_super_new, '请求ID', 'inner'
                             ).select(
        df_req_new['请求ID'], '素材ID', '监测类型', '数量', 'UV数')

    if df_m_c:
        df_m_c.show()
        df_m_c.coalesce(1).write.csv('material_count', header=True,
                                     mode='ignore')
        print('material_count file established successfully')
    else:
        print('material_count file established unsuccessfully')


def write_token_app_click_view(df_req, df_super):
    df_req_new = df_req.select('请求ID', '下游Token', 'APP名称', '广告位ID')
    df_super_new = df_super.select('请求ID', '监测类型', 'UserID')
    df_req_new = df_req_new.groupby('请求ID', '下游Token', 'APP名称', '广告位ID').count()
    df_super_new = df_super_new.groupby('请求ID', '监测类型').agg(
        count('请求ID').alias('数量'),
        countDistinct('UserID').alias('UV数'))
    df_click_view_count = df_req_new.join(df_super_new, '请求ID', 'inner'
                                          ).select(
        df_req_new['请求ID'], '下游Token', 'APP名称', '广告位ID', '数量', "UV数")

    if df_click_view_count:
        df_click_view_count.show()
        df_click_view_count.coalesce(1).write.csv('token_app_click_view',
                                                  header=True,
                                                  mode='ignore')
        print('token_app_click_view文件已生成')
    else:
        print('token_app_click_view文件生成失败')


def write_token_app_count(df_req, df_res, df_super):
    df_req_new = df_req.select('请求ID', '下游Token', 'APP名称', '广告位ID')
    df_res_new = df_res.select('请求ID', 'UserID')
    df_super_new = df_super.select('请求ID', '价格')
    df_req_new = df_req_new.groupby('请求ID', '下游Token', 'APP名称', '广告位ID').agg(
        count('请求ID').alias('请求数'),
        countDistinct('请求ID').alias('请求UV'))
    df_res_new = df_res_new.groupby('请求ID').agg(count('请求ID').alias('响应数'),
                                                countDistinct('UserID').alias(
                                                    '响应UV'))
    df_token_count1_2 = df_req_new.join(df_res_new, '请求ID', 'inner'
                                        ).select(
        df_req_new['请求ID'], '下游Token', 'APP名称', '广告位ID', '请求数', '请求UV',
        '响应数', '响应UV')

    df_token_count = df_token_count1_2.join(df_super_new, '请求ID', 'inner'
                                            ).select(
        df_token_count1_2['请求ID'], '下游Token', 'APP名称', '广告位ID', '请求数',
        '请求UV', '响应数', '响应UV', '价格')

    if df_token_count:
        df_token_count.show()
        df_token_count.coalesce(1).write.csv('token_app_count', header=True,
                                             mode='ignore')
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
    write_token_app_click_view(df_req, df_super)
    write_token_app_count(df_req, df_res, df_super)

    sc.stop()


if __name__ == '__main__':
    main()
