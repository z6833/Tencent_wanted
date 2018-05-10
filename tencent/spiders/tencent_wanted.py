# -*- coding: utf-8 -*-
import scrapy

# 导入待爬取字段名
from tencent.items import TencentItem, DetailsItem

class TencentWantedSpider(scrapy.Spider):
    name = 'tencent_wanted'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    base_url = 'https://hr.tencent.com/'

    def parse(self, response):

        # 获取页面中招聘信息在网页中位置节点
        node_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')

        # 匹配到下一页的按钮
        next_page = response.xpath('//a[@id="next"]/@href').extract_first()

        # 遍历节点，进入详情页，获取其他信息
        for node in node_list:
            # 实例化，填写数据
            item = TencentItem()

            item['position_name'] = node.xpath('./td[1]/a/text()').extract_first()
            item['position_link'] = node.xpath('./td[1]/a/@href').extract_first()
            item['position_type'] = node.xpath('./td[2]/text()').extract_first()
            item['wanted_number'] = node.xpath('./td[3]/text()').extract_first()
            item['work_location'] = node.xpath('./td[4]/text()').extract_first()
            item['publish_time' ] = node.xpath('./td[5]/text()').extract_first()

            yield item
            yield scrapy.Request(url=self.base_url + item['position_link'], callback=self.details)

        # 访问下一页信息
        yield scrapy.Request(url=self.base_url + next_page, callback=self.parse)

    def details(self, response):
        """
        对详情页信息进行抽取和解析
        :return:
        """
        item = DetailsItem()
        # 从详情页获取工作责任和工作技能两个字段名
        item['work_duties'] = ''.join(response.xpath('//ul[@class="squareli"]')[0].xpath('./li/text()').extract())
        item['work_skills'] = ''.join(response.xpath('//ul[@class="squareli"]')[1].xpath('./li/text()').extract())
        yield item

