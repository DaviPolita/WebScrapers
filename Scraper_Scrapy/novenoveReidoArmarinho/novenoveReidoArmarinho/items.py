# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NovenovereidoarmarinhoItem(scrapy.Item):
    # define the fields for your item here like:
    titulo = scrapy.Field()
    url = scrapy.Field()
    preço = scrapy.Field()
    marca = scrapy.Field()
    descrição = scrapy.Field()
    loja = scrapy.Field()
    categoria_1 = scrapy.Field()
    categoria_2 = scrapy.Field()
    categoria_3 = scrapy.Field()
    categoria_4 = scrapy.Field()
