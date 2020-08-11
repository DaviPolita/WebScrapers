# %%
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd


parte_1 = "https://www.medshop.com.br/buscapagina?fq=C%3a%2f"
parte_2 = "%2f&PS=25&sl=6e73a242-8211-4e21-9497-5e0ecffaed77&cc=24&sm=0&PageNumber="

# %%


def get_data(page_1, page_2):
    paginas = []

    rows = []

    data = []

    for i in tqdm(range(99)):
        pagina = page_1 + str(i).zfill(2) + page_2
        r = requests.get(pagina)
        soup = BeautifulSoup(r.content, "html.parser")
        if soup.find_all("li", {"layout": "6e73a242-8211-4e21-9497-5e0ecffaed77"}) == []:
            pass
        else:
            for n in tqdm(range(15)):
                pagina_f = pagina + str(n)
                r = requests.get(pagina_f)
                soup = BeautifulSoup(r.content, "html.parser")
                if soup.find_all("li", {"layout": "6e73a242-8211-4e21-9497-5e0ecffaed77"}) == []:
                    pass
                else:
                    print(pagina_f)
                    rows += soup.find_all("li",
                                          {"layout": "6e73a242-8211-4e21-9497-5e0ecffaed77"})

    for row in rows:
        d = dict()
        try:
            d["Nome"] = row.find(
                "p", {"class": "shelfProductName"}).text.strip().upper()
        except(TypeError, KeyError) as e:
            d["Nome"] = "None"
        try:
            d["Marca"] = row.find("a", {"class": "brand"}).text.strip()
        except(TypeError, KeyError) as e:
            d["Marca"] = "None"
        try:
            d["Pagina"] = row.select_one(".shelfProductName a")["href"]
        except(TypeError, KeyError) as e:
            d["Pagina"] = "None"
        if row.find("span", {"class": "bestPrice"}) == None:
            d["Preço"] = "Sem Estoque"
        else:
            d["Preço"] = row.find("span", {"class": "bestPrice"}).text.strip()

        data.append(d)
    return data


df = pd.DataFrame(get_data(parte_1, parte_2))


# %%


df.drop_duplicates(subset="Nome")

df.to_excel("preços4.xlsx")


# %%
