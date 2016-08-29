# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from jandan import settings
class JandanPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        '''
        :param item:
        :param info:
        :return:
        '''
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)
    def item_completed(self, results, item, info):
        '''
        :param results:
        :param item:
        :param info:
        :return:
        '''
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Item contains no image')
        return item
