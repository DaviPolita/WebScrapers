# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class TutorialPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect(
            "C:/Projetos_C/WebScrapers/Scraper_Scrapy/tutorial/tutorial/preços.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS preços_tb""")
        self.curr.execute("""
            CREATE TABLE preços_tb(
                titulo TEXT,
                preço TEXT,
                url TEXT,
                desc_curta TEXT,
                loja TEXT,
                categoria_1 TEXT,
                categoria_2 TEXT
            )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""
            INSERT INTO preços_tb 
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                          item["titulo"],
                          item["preço"],
                          item["url"],
                          item["desc_curta"],
                          item["loja"],
                          item["categoria_1"],
                          item["categoria_2"]
                          ))
        self.conn.commit()
