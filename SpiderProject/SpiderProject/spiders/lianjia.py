# -*- coding: utf-8 -*-
import re
import time

import xlrd
from scrapy import item
from bs4 import BeautifulSoup
import scrapy

from SpiderProject.items import RoomInfo


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['www.lianjia.com']
    start_url = 'http://sh.lianjia.com/ershoufang/{offset}'
    # http://sh.lianjia.com/ershoufang/d2rs%E6%B5%A6%E4%B8%9C
    # room_url = ""http://sh.lianjia.com/ershoufang/rs
    # http: // sh.lianjia.com / ershoufang / rs杨浦
    i=1
    # start_url = 'http://sh.lianjia.com/ershoufang'
    def start_requests(self):
        wb = xlrd.open_workbook("D:\\浦东新区小学.xls")
        sheet = wb.sheet_by_index(0)
        max_rows = sheet.nrows
        # max_rows = 100
        for i in range(1, max_rows):
            school = sheet.cell_value(i, 3)  #
            if school is not None and school is not '':
                district = sheet.cell_value(i, 5)  # 学期
                u = self.start_url.format(offset=('d' + str(self.i) + 'rs'+district))
                request=scrapy.Request(u, meta={'download_timeout': 30}, callback=self.parse, dont_filter=True)
                item = RoomInfo()
                item['school'] = school
                request.meta['item'] = item
                yield request


    def parse(self, response):
        # item = RoomInfo()
        # item['id']=11111111111111
        # print('111111111111111111111111')
        # yield item
        try:
            item = RoomInfo()
            sitem = response.meta['item']
            print("-----------------------------",sitem['school'])
            # print(response.url)
            soup = BeautifulSoup(response.text, "lxml")
            # query result
            search_result = soup.find(class_="search-result")
            if search_result is not None:
                # print("无房源")
            # else:
                # print(search_result.text)
                ul = soup.find(class_="js_fang_list")
                # print(type(ul))
                li = ul.find_all("li")
                if len(li)>0:
                    # print("无房源")
                # else:
                    for info in li:
                        # Description
                        description = info.find(class_="text link-hover-green js_triggerGray js_fanglist_title").text
                        id = info.find(class_="text link-hover-green js_triggerGray js_fanglist_title")['key']
                        # category1
                        type1 = info.find(class_="info-col row1-text").text
                        type1 = type1.strip().replace("	", "").replace("\n", "")
                        typelist = type1.split("|")
                        # category2
                        type2 = info.find(class_="info-col row2-text").text
                        type2 = type2.strip().replace("	", "").replace("\n", "")
                        typelist2 = type2.split("|")
                        # price
                        price = info.find(class_="total-price strong-num").text
                        unit = info.find(class_="unit").text
                        if unit is None or unit == "":
                            unit = "万"
                        # unitprice
                        unitprice = info.find(class_="info-col price-item minor").text
                        if unitprice is None or unitprice == "":
                            unitprice = "万"
                        # remark
                        remark = info.find(class_="property-tag-container").text
                        lens = len(typelist)
                        if lens != 4:
                            room_ore = ""
                        else:
                            room_ore = typelist[3]
                        len2 = len(typelist2)
                        if len2 !=4:
                            buildyear = ""
                        else:
                            buildyear=typelist2[3]
                        item["id"]=id
                        item["orientation"] = room_ore
                        item["title"] = description.strip().replace(' ','')
                        item["housetype"] = typelist[0].replace(' ','')
                        item["buildingarea"] = typelist[1].replace(' ','')
                        item["floor"] = typelist[2].replace(' ','')
                        item["sublocation"] = typelist2[0].replace(' ','')
                        item["location"] = typelist2[1].replace(' ','')
                        item["buildyear"] = buildyear
                        item["totalprice"] = price.strip().lstrip().replace(' ','')
                        item["perprice"] = unitprice.lstrip().rstrip().replace(' ','').replace('单价','').replace('/平','').replace('元','')
                        item["remark"] = remark.strip().lstrip().replace(' ','')

                        item['tax']=""
                        item['district'] = typelist2[1].replace(' ','')
                        item['subway'] = ""
                        item['detailurl'] = "http://sh.lianjia.com/ershoufang/"+item["id"] + ".html"
                        item['offline'] = ""
                        item['timeflag'] = time.strftime('%Y-%m-%d',time.localtime(time.time()))
                        item['issail'] = "N"
                        item['location'] = typelist2[2].replace(' ','')
                        item['school']=sitem['school']
                        # print(item)



                        yield item
                    divPage = soup.find(class_="c-pagination")
                    aPage = divPage.findAll("a")
                    for a1 in aPage:
                        if a1.contents[0] == "下一页":
                            self.i=self.i+1
                            request=scrapy.Request(re.sub('d.rs','d'+str(self.i)+'rs',response.url),meta={'download_timeout':30},callback=self.parse,dont_filter=True)
                            nitem = RoomInfo()
                            nitem['school'] = sitem['school']
                            request.meta['item'] = nitem
                            yield request
        except AttributeError as e:
            print(e)
        except Exception as e:
            print(e)
