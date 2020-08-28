import scrapy
from ..items import NovenoveFiebItem


class FiebSpider(scrapy.Spider):
    name = "fieb"
    start_urls = [
        "http://www.fieb.org.br/guia/Resultado_Consulta.aspx?localizacao=&ordenacao=ind_razao_social&page=0&consulta=Consulta+B%u00e1sica&consulta=Consulta+B%u00e1sica&consulta=Consulta+B%u00e1sica&consulta=Consulta+B%u00e1sica"
    ]

    next_page = 1

    def parse(self, response):

        next_url = "http://www.fieb.org.br/guia/Resultado_Consulta.aspx?localizacao=&ordenacao=ind_razao_social&page=" + \
            str(self.next_page) + "&consulta=Consulta+B%u00e1sica&consulta=Consulta+B%u00e1sica&consulta=Consulta+B%u00e1sica&consulta=Consulta+B%u00e1sica"

        #label-consulta-3 > td > div > span > a

        item = NovenoveFiebItem()

        all_url = response.xpath(
            "//*[@id='label-consulta-3']/td/div/span/a/@href").getall()

        for url in all_url:
            page_url = "http://www.fieb.org.br/guia/" + url
            item["url"] = page_url
            item2 = item.copy()
            yield response.follow(item["url"], callback=self.parse2, meta={'item': item2})

        if self.next_page < 10:
            self.next_page += 1
            yield response.follow(next_url, callback=self.parse)

    def parse2(self, response):
        item = response.meta['item']

        item["razao_social"] = response.css(
            ".razaoSocial::text").get(default="Vazio").strip()
        item["cnpj"] = response.xpath(
            '//*[@id="divDadosIndustria"]/text()[3]').get(default="Vazio").strip()
        item["inscricao_estadual"] = response.xpath(
            '//*[@id="divDadosIndustria"]/text()[5]').get(default="Vazio").strip()
        item["nome_fantasia"] = response.xpath(
            '//*[@id="divDadosIndustria"]/text()[9]').get(default="Vazio").strip()
        item["cnae"] = response.css(
            "#ContentPlaceHolder1_generalContent_rptIndustria_lblCNAE_0::text").get(default="Vazio").strip()
        item["descricao_cnae"] = response.css(
            "#ContentPlaceHolder1_generalContent_rptIndustria_lblDescricaoCNAE_0::text").get(default="Vazio").strip()
        item["comercio_int"] = response.css(
            "#ContentPlaceHolder1_generalContent_rptIndustria_lblComercio_0::text").get(default="Vazio").strip()
        item["logradouro"] = response.css(
            "#ContentPlaceHolder1_generalContent_rptIndustria_lblLogradouro_0::text").get(default="Vazio").strip()
        item["bairro"] = response.css(
            "#ContentPlaceHolder1_generalContent_rptIndustria_lblBairro_0::text").get(default="Vazio").strip()
        item["municipio"] = response.css(
            "#ContentPlaceHolder1_generalContent_rptIndustria_lblMunicipio_0::text").get(default="Vazio").strip()
        item["estado"] = response.css(
            "#ContentPlaceHolder1_generalContent_rptIndustria_lblEstado_0::text").get(default="Vazio").strip()
        item["cep"] = response.css(
            "#ContentPlaceHolder1_generalContent_rptIndustria_lblCEP_0::text").get(default="Vazio").strip()
        item["telefone"] = response.css(
            "#ContentPlaceHolder1_generalContent_rptIndustria_lblTelefone_0::text").get(default="Vazio").strip()
        item["email"] = response.css(
            "#divDadosIndustria a::text").get(default="Vazio").strip()
        item["site"] = response.xpath(
            '//*[@id="divDadosIndustria"]/a[2]/@href').get(default="Vazio").strip()
        item["tudo"] = response.css("#divDadosIndustria *::text").getall()

        yield item
