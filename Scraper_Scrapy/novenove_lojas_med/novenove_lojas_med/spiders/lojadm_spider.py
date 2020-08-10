import scrapy
from ..items_lojadm import NovenoveLojasMedItem


class LojaDMSpider(scrapy.Spider):
    name = "lojadm"
    start_urls = [
        "https://www.lojadomedico.com.br/buscapagina?fq=C%3a%2f1000000%2f&PS=15&sl=34339203-0e23-4596-bcf5-3beb6a0b3e90&cc=15&sm=0&PageNumber=1"
    ]

    next_page = 1
    cat_number = 1

    def parse(self, response):

        next_url = "https://www.lojadomedico.com.br/buscapagina?fq=C%3a%2f10000" + str(self.cat_number).zfill(2) + "%2f&PS=15&sl=34339203-0e23-4596-bcf5-3beb6a0b3e90&cc=15&sm=0&PageNumber=" + \
            str(self.next_page)

        if response.status == 500:
            if self.cat_number < 99:
                self.cat_number += 1
                self.next_page = 1
                yield response.follow(next_url, callback=self.parse)

        else:
            item = NovenoveLojasMedItem()

            all_url = response.css(".no-gutters::attr(href)").getall()

            if all_url:
                for url in all_url:
                    item["url"] = url
                    item2 = item.copy()
                    yield response.follow(item["url"], callback=self.parse2, meta={'item': item2})

                self.next_page += 1
                yield response.follow(next_url, callback=self.parse)

            else:
                if self.cat_number < 99:
                    self.cat_number += 1
                    self.next_page = 1
                    yield response.follow(next_url, callback=self.parse)

    def parse2(self, response):
        item = response.meta['item']

        item["titulo"] = response.css(
            ".productName::text").get(default="Vazio").strip()
        item["preço"] = response.css(
            ".skuBestPrice::text").get(default="Vazio").strip()
        item["desc_curta"] = response.css(
            ".productDescriptionShort::text").get(default="Vazio").strip()
        item["loja"] = response.css(
            ".bread-crumb li:nth-child(1) span::text").get(default="Vazio")
        item["categoria_1"] = response.css(
            ".bread-crumb li:nth-child(2) span::text").get(default="Vazio")
        item["categoria_2"] = response.css(
            ".bread-crumb li:nth-child(3) span::text").get(default="Vazio")

        yield item
