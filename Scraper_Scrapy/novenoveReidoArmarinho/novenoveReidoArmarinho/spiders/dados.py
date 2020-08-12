# import sqlite3
# import pandas as pd
# # Create your connection.
# cnx = sqlite3.connect('rei_do_armarinho.db')

# df = pd.read_sql_query("SELECT * FROM produtos_tb", cnx)

# # df.to_csv("preços.csv")
# df.to_excel("produtos.xlsx")


# # print(len(test))

# def name_img(test):
#     if len(test) == 1:
#         image_1 = test[0]["path"]
#         image_2 = "nope"
#         return [image_1, image_2]
#     else:
#         image_1 = test[0]["path"]
#         image_2 = test[1]["path"]
#         return [image_1, image_2]


# print(name_img(test)[1])


# #     for i in range(len(test)):


# # dic = {}
# # for i in range(len(test)):
# #     name = "image" + str(i)
# #     # dic.append(name)
# #     dic[f"{name}"] = test[i]["path"]
# #     # print(dic[i])

# # print(dic)

# # # image = test[i]["path"]
# # # print(image)
