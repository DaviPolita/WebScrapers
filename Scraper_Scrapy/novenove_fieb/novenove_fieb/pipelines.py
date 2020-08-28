# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
import re


class NovenoveFiebPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect(
            "C:/Projetos_C/WebScrapers/Scraper_Scrapy/novenove_fieb/novenove_fieb/spiders/lista_fieb.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS empresas_tb""")
        self.curr.execute("""
            CREATE TABLE empresas_tb(
                url TEXT,
                razao_social TEXT,
                cnpj TEXT,
                inscricao_estadual TEXT,
                nome_fantasia TEXT,
                cnae TEXT,
                descricao_cnae TEXT,
                lista_prod TEXT,
                lista_ins TEXT,
                num_funcionarios TEXT,
                comercio_int TEXT,
                logradouro TEXT,
                bairro TEXT,
                municipio TEXT,
                estado TEXT,
                cep TEXT,
                telefone TEXT,
                email TEXT,
                site TEXT,
                tudo TEXT
            )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        string2 = item["tudo"]
        string2 = [item.strip() for item in string2]
        string2 = list(filter(None, string2))
        string2 = " ".join(string2)
        lista_prod = re.search(
            'Lista de Produtos:(.*)Lista de Insumos:', string2)
        lista_ins = re.search('Lista de Insumos:(.*)Número Total', string2)
        num_funcionarios = re.search(
            'Total de Funcionários:(.*)Quanto ao', string2)

        self.curr.execute("""
            INSERT INTO empresas_tb 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                          item["url"],
                          item["razao_social"],
                          item["cnpj"],
                          item["inscricao_estadual"],
                          item["nome_fantasia"],
                          item["cnae"],
                          item["descricao_cnae"],
                          lista_prod.group(1),
                          lista_ins.group(1),
                          num_funcionarios.group(1),
                          item["comercio_int"],
                          item["logradouro"],
                          item["bairro"],
                          item["municipio"],
                          item["estado"],
                          item["cep"],
                          item["telefone"],
                          item["email"],
                          item["site"],
                          string2,))
        self.conn.commit()
