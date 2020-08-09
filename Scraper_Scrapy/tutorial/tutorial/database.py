import sqlite3

conn = sqlite3.connect(
    "C:/Projetos_C/WebScrapers/Scraper_Scrapy/tutorial/tutorial/myquotes.db")
curr = conn.cursor()

# curr.execute("""
#     CREATE TABLE quotes_tb(
#         title TEXT,
#         author TEXT,
#         tag TEXT
#     )
# """)

curr.execute("""
    INSERT INTO quotes_tb VALUES ("Texto aleatorio", "eu mesmo", "python")
    """)


conn.commit()
conn.close()
