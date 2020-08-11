import sqlite3
import pandas as pd
# Create your connection.
cnx = sqlite3.connect('preços.db')

df = pd.read_sql_query("SELECT * FROM lojadm_tb", cnx)

# df.to_csv("preços.csv")
df.to_excel("preços.xlsx")
