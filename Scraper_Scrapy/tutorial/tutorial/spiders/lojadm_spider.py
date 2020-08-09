import scrapy
from ..items_med import TutorialItem


class LojaDMSpider(scrapy.Spider):
    name = "lojadm"
    start_urls = [
        "https://www.lojadomedico.com.br/buscapagina?fq=C%3a%2f1000032%2f&PS=15&sl=34339203-0e23-4596-bcf5-3beb6a0b3e90&cc=15&sm=0&PageNumber=1"
    ]

    def parse(self, response):
        item = TutorialItem()

        all_div = response.css(".material-medico")
        for div in all_div:
            item["titulo"] = div.css(".fs-18::text").get(default="Vazio")
            item["preço"] = div.css(".lh-10::text").get(default="Vazio")
            item["url"] = div.css(
                ".no-gutters").xpath('@href').get(default="Vazio")
            item2 = item.copy()
            yield response.follow(item["url"], callback=self.parse2, meta={'item': item2})

    def parse2(self, response):
        item = response.meta['item']

        item["desc_curta"] = response.css(
            ".productDescriptionShort::text").get(default="Vazio")
        item["loja"] = response.css(
            ".bread-crumb li:nth-child(1) span::text").get(default="Vazio")
        item["categoria_1"] = response.css(
            ".bread-crumb li:nth-child(2) span::text").get(default="Vazio")
        item["categoria_2"] = response.css(
            ".bread-crumb li:nth-child(3) span::text").get(default="Vazio")

        yield item
