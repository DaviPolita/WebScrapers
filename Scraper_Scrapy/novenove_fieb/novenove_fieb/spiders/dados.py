import sqlite3
import pandas as pd
# Create your connection.
cnx = sqlite3.connect('lista_fieb.db')

df = pd.read_sql_query("SELECT * FROM empresas_tb", cnx)

# df.to_csv("preços.csv")
df.to_excel("empresas.xlsx")
