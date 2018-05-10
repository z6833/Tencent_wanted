# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from tencent.items import TencentItem, DetailsItem
class TencentPipeline(object):
    def open_spider(self, spider):
        """
        爬虫运行时，执行的方法
        :param spider:
        :return:
        """
        self.file = open('tenc_wanted_2.json', 'w', encoding='utf-8')
        self.file_detail = open('tenc_wanted_detail.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):

        content = json.dumps(dict(item), ensure_ascii=False)

        # 判断数据来源于哪里（是哪个类的实例），写入对应的文件
        if isinstance(item, TencentItem):
            self.file.write(content + '\n')

        if isinstance(item, DetailsItem):
            self.file_detail.write(content + '\n')

        return item

    def close_spider(self, spider):
        """
        爬虫运行结束后执行的方法
        :param spider:
        :return:
        """
        self.file.close()
        self.file_detail.close()
