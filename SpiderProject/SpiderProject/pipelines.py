# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pyodbc

# store data into sqlserver
from scrapy.exceptions import DropItem


# save to sqlserver

class SQlserverPipeline(object):
    def __init__(self, connectstr):
        self.connectstr = connectstr

    @classmethod
    def from_crawler(cls, crawler):
        return cls(connectstr=crawler.settings.get('CONNECTSTR'))

    def process_item(self, item, spider):
        if item['id']:
            cnxn = pyodbc.connect(self.connectstr)
            cursor = cnxn.cursor()

            cursor.execute("select id,totalprice,perprice from [HouseInfo] where id='" + item['id'] + "'")
            row = cursor.fetchone()
            if row:
                # updatesql
                if row[1]!=item['totalprice']:
                    updatesql = "update HouseInfo set perprice='" + item['perprice'] + "',totalprice='" + item[
                        'totalprice'] + "' where id='" + item['id'] + "'"
                    cursor.execute(updatesql)
            else:
                #
                insertsql = '''insert into HouseInfo (id,title,housetype,buildingarea,orientation,buildyear,perprice,totalprice,tax,sfloor,district,subway,detailurl,soffline,timeflag,issail,remark,sublocation,location,statuscode,school) values ('''
                insertsql = insertsql + "'" + item['id'] + "',"
                insertsql = insertsql + "'" + item['title'] + "',"
                insertsql = insertsql + "'" + item['housetype'] + "',"
                insertsql = insertsql + "'" + item['buildingarea'] + "',"
                insertsql = insertsql + "'" + item['orientation'] + "',"
                insertsql = insertsql + "'" + item['buildyear'] + "',"
                insertsql = insertsql + "'" + item['perprice'] + "',"
                insertsql = insertsql + "'" + item['totalprice'] + "',"
                insertsql = insertsql + "'" + item['tax'] + "',"
                insertsql = insertsql + "'" + item['floor'] + "',"
                insertsql = insertsql + "'" + item['district'] + "',"
                insertsql = insertsql + "'" + item['subway'] + "',"
                insertsql = insertsql + "'" + item['detailurl'] + "',"
                insertsql = insertsql + "'" + item['offline'] + "',"
                insertsql = insertsql + "'" + item['timeflag'] + "',"
                insertsql = insertsql + "'" + item['issail'] + "',"
                insertsql = insertsql + "'" + item['remark'] + "',"
                insertsql = insertsql + "'" + item['sublocation'] + "',"
                insertsql = insertsql + "'" + item['location'] + "',"
                insertsql = insertsql + "'0',"
                insertsql = insertsql + "'" + item['school'] + "')"
                print("===================================================",insertsql)
                cursor.execute(insertsql)
                cnxn.commit()
            cursor.close()
            cnxn.close()
            return item
        else:
            raise DropItem("room key is missing")

class FileStorePipeline(object):
    def __init__(self,filepath):
        self.filepath = filepath
        print("-------------------",self.filepath)
        self.file = open(filepath, 'wb')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(filepath=crawler.settings.get('FILENAME'))

    def process_item(self, item, spider):
        if item['id']:
            insertsql = '''insert into HouseInfo (id,title,housetype,buildingarea,orientation,buildyear,perprice,totalprice,tax,sfloor,district,subway,detailurl,soffline,timeflag,issail,remark,sublocation,location,statuscode,school) values ('''
            insertsql = insertsql + "'" + item['id'] + "',"
            insertsql = insertsql + "'" + item['title'] + "',"
            insertsql = insertsql + "'" + item['housetype'] + "',"
            insertsql = insertsql + "'" + item['buildingarea'] + "',"
            insertsql = insertsql + "'" + item['orientation'] + "',"
            insertsql = insertsql + "'" + item['buildyear'] + "',"
            insertsql = insertsql + "'" + item['perprice'] + "',"
            insertsql = insertsql + "'" + item['totalprice'] + "',"
            insertsql = insertsql + "'" + item['tax'] + "',"
            insertsql = insertsql + "'" + item['floor'] + "',"
            insertsql = insertsql + "'" + item['district'] + "',"
            insertsql = insertsql + "'" + item['subway'] + "',"
            insertsql = insertsql + "'" + item['detailurl'] + "',"
            insertsql = insertsql + "'" + item['offline'] + "',"
            insertsql = insertsql + "'" + item['timeflag'] + "',"
            insertsql = insertsql + "'" + item['issail'] + "',"
            insertsql = insertsql + "'" + item['remark'] + "',"
            insertsql = insertsql + "'" + item['sublocation'] + "',"
            insertsql = insertsql + "'" + item['location'] + "',"
            insertsql = insertsql + "'0',"
            insertsql = insertsql + "'" + item['school'] + "')"
            print("===================================================",insertsql)
            insertsql = insertsql+'\n'
            self.file.write(insertsql.encode(encoding='utf-8'))
            return item
        else:
            raise DropItem("room key is missing")