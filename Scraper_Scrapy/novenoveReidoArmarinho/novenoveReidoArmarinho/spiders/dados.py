import sqlite3
import pandas as pd
# Create your connection.
cnx = sqlite3.connect('rei_do_armarinho.db')

df = pd.read_sql_query("SELECT * FROM produtos_tb", cnx)

# df.to_csv("preços.csv")
df.to_excel("produtos.xlsx")
