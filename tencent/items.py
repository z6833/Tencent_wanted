# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 职位名称
    position_name = scrapy.Field()
    # 职位类别
    position_type = scrapy.Field()
    # 招聘人数
    wanted_number = scrapy.Field()
    # 工作地点
    work_location = scrapy.Field()
    # 发布时间
    publish_time = scrapy.Field()
    # 详情信息
    position_link = scrapy.Field()

class DetailsItem(scrapy.Item):
    """
    将详情页提取到的数据另外保存到一个文件中
    """
    # 工作职责
    work_duties = scrapy.Field()
    # 工作要求
    work_skills = scrapy.Field()
