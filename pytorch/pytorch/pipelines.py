# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
from scrapy.http import Request


class PytorchPipeline(object):
    def process_item(self, item, spider):
        return item


class htmlPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        url = request.url
        name = url.split('/')[-1]
        a = url.split('/')[6:-1]
        if a:
            path_ss = 'full/%s' % ('/'.join(a))
        else:
            path_ss = 'full'
        return '%s/%s' % (path_ss, name)
