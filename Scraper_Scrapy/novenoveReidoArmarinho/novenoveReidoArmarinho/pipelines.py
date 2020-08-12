# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class NovenovereidoarmarinhoPipelineSQL:
    # rei do armarinho
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect(
            "C:/Projetos_C/WebScrapers/Scraper_Scrapy/novenoveReidoArmarinho/novenoveReidoArmarinho/spiders/rei_do_armarinho.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS produtos_tb""")
        self.curr.execute("""
            CREATE TABLE produtos_tb(
                titulo TEXT,
                preço TEXT,
                url TEXT,
                marca TEXT,
                descrição TEXT,
                loja TEXT,
                categoria_1 TEXT,
                categoria_2 TEXT,
                categoria_3 TEXT,
                categoria_4 TEXT,
                imagem_1 TEXT,
                imagem_2 TEXT
            )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    # def name_img(item):
    #     if len(item["images"]) == 1:
    #         image_1 = item["images"][0]["path"]
    #         image_2 = ""
    #         return [image_1, image_2]
    #     else:
    #         image_1 = item["images"][0]["path"]
    #         image_2 = item["images"][1]["path"]
    #         return [image_1, image_2]

    def store_db(self, item):
        # tranforma uma lista de str em uma unica str
        desc = " ".join(item["descrição"])
        desc = desc.replace(" .", "")

        image_1 = ""
        image_2 = ""

        if len(item["images"]) == 1:
            image_1 = item["images"][0]["path"]
            image_2 = ""

        if len(item["images"]) > 1:
            image_1 = item["images"][0]["path"]
            image_2 = item["images"][1]["path"]

        self.curr.execute("""
            INSERT INTO produtos_tb 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                          item["titulo"],
                          item["preço"],
                          item["url"],
                          item["marca"],
                          desc,
                          item["loja"],
                          item["categoria_1"],
                          item["categoria_2"],
                          item["categoria_3"],
                          item["categoria_4"],
                          image_1,
                          image_2
                          ))
        self.conn.commit()
# teste
