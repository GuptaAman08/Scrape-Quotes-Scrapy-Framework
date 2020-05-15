# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Extracted data => temporary containers (items) => Pipeline => SQL/Mongo Database
import sqlite3
from pymongo import MongoClient


class ScrapeQoutesPipeline(object):
    
    def __init__(self):
        self.create_connection()
        self.create_table()


    def create_connection(self):
        self.conn = sqlite3.connect("quotes.db")
        self.cur = self.conn.cursor()


    def create_table(self):
        # Drop the table if already existcls
        self.cur.execute("""DROP TABLE IF EXISTS quotes_tb""")

        self.cur.execute("""
                    create table quotes_tb(
                        title text,
                        author text,
                        tag text
                    )
                """)


    def store_date(self, item):
        self.cur.execute("""
                insert into quotes_tb values (?,?,?)""",(item["title"][0], item["author"][0], item["tag"][0])
            )

        self.conn.commit()

    def process_item(self, item, spider):
        self.store_date(item)
        # print(item["title"])
        return item


# Use Below code for storing in mongoDB
class ScrapeQuotes(object):
    def __init__(self):
        self.conn = MongoClient("mongodb://localhost:27017/")
        self.db = self.conn["qoutesDB"]
        self.collection = self.db["qoutes_table"]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item