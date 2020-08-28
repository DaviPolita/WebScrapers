# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NovenoveFiebItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    razao_social = scrapy.Field()
    cnpj = scrapy.Field()
    inscricao_estadual = scrapy.Field()
    nome_fantasia = scrapy.Field()
    cnae = scrapy.Field()
    descricao_cnae = scrapy.Field()
    comercio_int = scrapy.Field()
    logradouro = scrapy.Field()
    bairro = scrapy.Field()
    municipio = scrapy.Field()
    estado = scrapy.Field()
    cep = scrapy.Field()
    telefone = scrapy.Field()
    email = scrapy.Field()
    site = scrapy.Field()
    tudo = scrapy.Field()
