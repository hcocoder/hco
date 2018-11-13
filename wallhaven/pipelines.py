# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests

import scrapy
class KkpPipeline(object):

    def process_item(self, item, spider):

        ite=list(dict(item).values())

        for url in ite:
            print("开始下载壁纸")
            req = requests.get(url)
            name=os.path.basename(url)

            os.chdir('C:/Users/Administrator/Pictures/Camera Roll')
            f=open(name,"ab")
            f.write(req.content)
            print(name+'下载完成！')
        print('下载完毕！')
        return item
