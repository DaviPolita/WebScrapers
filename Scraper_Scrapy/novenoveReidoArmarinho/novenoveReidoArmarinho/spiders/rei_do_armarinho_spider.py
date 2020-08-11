import scrapy
from ..items import NovenovereidoarmarinhoItem


class LojaDMSpider(scrapy.Spider):

    name = "rei_do_armarinho"
    start_urls = [
        "https://www.reidoarmarinho.com.br/buscapagina?fq=C%3a%2f80%2f&PS=12&sl=ef3fcb99-de72-4251-aa57-71fe5b6e149f&cc=4&sm=0&PageNumber=1"
    ]

    next_page = 1
    cat_number = 1

    def parse(self, response):

        next_url = "https://www.reidoarmarinho.com.br/buscapagina?fq=C%3a%2f80%2f&PS=12&sl=ef3fcb99-de72-4251-aa57-71fe5b6e149f&cc=4&sm=0&PageNumber=" + \
            str(self.next_page)

        if response.status == 500:
            if self.cat_number < 99:
                self.cat_number += 1
                self.next_page = 1
                yield response.follow(next_url, callback=self.parse)

        else:
            item = NovenovereidoarmarinhoItem()

            all_url = response.css(".product-name a::attr(href)").getall()

            if all_url:
                for url in all_url:
                    item["url"] = url
                    item2 = item.copy()
                    yield response.follow(item["url"], callback=self.parse2, meta={'item': item2})

                self.next_page += 1
                yield response.follow(next_url, callback=self.parse)

            # else:
            #     if self.cat_number < 99:
            #         self.cat_number += 1
            #         self.next_page = 1
            #         yield response.follow(next_url, callback=self.parse)

    def parse2(self, response):
        item = response.meta['item']

        item["titulo"] = response.css(
            ".productName::text").get(default="Vazio").strip()
        item["preço"] = response.css(
            ".skuBestPrice::text").get(default="Vazio").strip()
        item["marca"] = response.css(
            ".brand::text").get(default="Vazio").strip()
        item["descrição"] = response.css(
            ".productDescription *::text").getall()
        item["loja"] = response.css(
            "#box-bread-brumb li:nth-child(1) span::text").get(default="Vazio")
        item["categoria_1"] = response.css(
            "#box-bread-brumb li:nth-child(2) span::text").get(default="Vazio")
        item["categoria_2"] = response.css(
            "#box-bread-brumb li:nth-child(3) span::text").get(default="Vazio")
        item["categoria_3"] = response.css(
            "#box-bread-brumb li:nth-child(4) span::text").get(default="Vazio")
        item["categoria_4"] = response.css(
            "#box-bread-brumb li:nth-child(5) span::text").get(default="Vazio")

        yield item


# x = list(set(response.xpath('//*[(@id = "botaoZoom")]/@rel').getall()))
