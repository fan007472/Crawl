# -*-coding:utf-8-*-
import pyodbc
import re

import time
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, orm
#
# from sqlalchemy import create_engine
#
# from SpiderProject.settings import CONNECTSTR
#
# connectstr = CONNECTSTR
# # print(connectstr)
# cnxn = pyodbc.connect(connectstr)
# # cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='gbk')
# # cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='gbk')
# # cnxn.setencoding(encoding='gbk')
#
# cursor = cnxn.cursor()
#
# cursor.execute("insert into HouseInfo (id,title,housetype,buildingarea,orientation,buildyear,perprice,totalprice,tax,sfloor,district,subway,detailurl,soffline,timeflag,issail,remark,sublocation,location,statuscode) values ('sh4873528','厨卫全明，卧室带阳台，出行方便，黄金楼层','2室1厅','53.28平',' 朝南',' 1986年建','单价78828元/平','420万','','中区/6层','浦东','','http://sh.lianjia.com/ershoufang/sh4873528.html','','2017-12-20','N','距离4号线浦东大道站494米有钥匙','陈家门小区','源深','0')")
# # row = cursor.fetchone()
# # if row:
# #     print('----------' + str(row))
# # else:
# #     print('222222222222222')
# cnxn.commit()
#
# cursor.close()
# cnxn.close()

#
# Base = declarative_base()
#
# class KPI(Base):
#     __tablename__='D_KPI'
#     KPI = Column(Integer,primary_key=True)
#     KPI_ID=Column(String)
#     KPI_SUB_ID=Column(String)
#     KPI_DESC=Column(String)
#     DEP=Column(String)
#     PROD_LINE=Column(String)
#     KPI_VALUE=Column(String)
#
# try:
#     engine = create_engine("mssql+pyodbc://ssa:Password01@10.242.192.26:1433/EReportSolution?driver=SQL+Server+Native+Client+10.0")
#
#     Session = orm.sessionmaker(bind=engine)
#     ses = Session()
#
#     kpis = ses.query(KPI).all()
#     for i in kpis:
#         print(i)
#
#     ses.commit()
# except ImportError:
#     raise RuntimeError()
#
b='----------'
a = '''123123'''+b+\
        '''123123,0'''+\
''',0)'''
# print(a)


C='陈家门小区 '
C=C.replace(' ','')
print('1'+C+'1')

time.strftime('%Y-%m-%d',time.localtime(time.time()))
print(time.strftime('%Y-%m-%d',time.localtime(time.time())))

str1 = "http://sh.lianjia.com/ershoufang/d1rs%E5%8D%9A%E5%85%B4%E8%B7%AF467%E5%BC%84"
m = re.sub('.*(d.rs).*','d2rs',str1)
print(m)

str1.replace('.*(d.rs).*','d2rs')
print(str1)

reobj = re.compile('.*(d.rs).*')
print(reobj.sub('d2rs', str1))

print(re.sub('d.rs','d2123rs',str1))