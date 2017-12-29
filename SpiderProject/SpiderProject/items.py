# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class RoomInfo(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    title = Field()
    housetype = Field()
    buildingarea = Field()
    orientation = Field()
    buildyear = Field()
    perprice = Field()
    totalprice = Field()
    tax = Field()
    floor = Field()
    district = Field()
    subway = Field()
    detailurl = Field()
    offline = Field()
    timeflag = Field()
    issail = Field()
    remark = Field()
    sublocation = Field()
    location = Field()
    school = Field()


