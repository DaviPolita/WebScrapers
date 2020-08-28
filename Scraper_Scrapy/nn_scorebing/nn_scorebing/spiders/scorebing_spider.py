import scrapy
from ..items import NnScorebingItem


class LojaDMSpider(scrapy.Spider):

    name = "scorebing"
    start_rows = [
        "https://www.scorebing.com/fixtures/20200728/p.1"
    ]
    pag = 1

    def parse(self, response):

        item = NnScorebingItem()

        # ano = range(2020, 2021)
        # mes = range(1, 8)
        # dia = range(1, 32)

        # next_row = self.start_rows[0] + str(a) + str(m).zfill(2) + \
        #                     str(d).zfill(2) + "/p." + str(self.pag)

        # for a in ano:
        #     for m in mes:
        #         for d in dia:
        #             if self.pag < 10:

        all_rows = response.css(".diary-table tbody tr").getall()
        # all_rows = response.css(".diary-table tbody tr td a::text").get()
        # all_rows = response.css(".diary-table tbody tr td::text").getall()

        # response.css("td:nth-child(1) a::text").getall()

        if all_rows:
            for row in all_rows:
                item["liga"] = row.css("td:nth-child(1) a::text").get()
                item["data_jogo"] = row.css("td:nth-child(2)::text").get()
                item["time_casa"] = row.css(".BR0 a::text").get()
                item["placar"] = row.css(".PR0::text").get()
                item["time_visitante"] = row.css(
                    "td:nth-child(5) a::text").get()
                item["linha_tempo"] = row.xpath(
                    "//*[(@id = 'race_timeLine')]//span@title").getall()
                yield item

                # self.pag += 1
                # yield response.follow(next_row, callback=self.parse)

                # else:
                #     if self.cat_number < 99:
                #         self.cat_number += 1
                #         self.next_page = 1
                #         yield response.follow(next_row, callback=self.parse)

    # def parse2(self, response):
    #     item = response.meta['item']

    #     item["titulo"] = response.css(
    #         ".productName::text").get(default="Vazio").strip()
    #     item["preço"] = response.css(
    #         ".skuBestPrice::text").get(default="Vazio").strip()
    #     item["marca"] = response.css(
    #         ".brand::text").get(default="Vazio").strip()
    #     item["descrição"] = response.css(
    #         ".productDescription *::text").getall()
    #     item["loja"] = response.css(
    #         "#box-bread-brumb li:nth-child(1) span::text").get(default="Vazio")
    #     item["categoria_1"] = response.css(
    #         "#box-bread-brumb li:nth-child(2) span::text").get(default="Vazio")
    #     item["categoria_2"] = response.css(
    #         "#box-bread-brumb li:nth-child(3) span::text").get(default="Vazio")
    #     item["categoria_3"] = response.css(
    #         "#box-bread-brumb li:nth-child(4) span::text").get(default="Vazio")
    #     item["categoria_4"] = response.css(
    #         "#box-bread-brumb li:nth-child(5) span::text").get(default="Vazio")
    #     item["image_rows"] = list(
    #         set(response.xpath('//*[(@id = "botaoZoom")]/@rel').getall()))

    #     yield item


# x = list(set(response.xpath('//*[(@id = "botaoZoom")]/@rel').getall()))
# teste
