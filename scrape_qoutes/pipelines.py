# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Extracted data => temporary containers (items) => Pipeline => SQL/Mongo Database
import sqlite3
from pymongo import MongoClient


class ScrapeQoutesPipeline(object):

    def process_item(self, item, spider):
        self.store_date(item)
        # print(item["title"])
        return item

