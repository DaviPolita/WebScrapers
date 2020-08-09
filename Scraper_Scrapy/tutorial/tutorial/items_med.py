# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    titulo = scrapy.Field()
    preço = scrapy.Field()
    url = scrapy.Field()
    desc_curta = scrapy.Field()
    loja = scrapy.Field()
    categoria_1 = scrapy.Field()
    categoria_2 = scrapy.Field()
