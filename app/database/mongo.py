from pymongo import MongoClient

#Faz a coneção com o localhost
cliente = MongoClient(
    "mongodb://localhost:27017/"
)
#Seleciona o banco de dados
db = cliente["project_web_scraping"]

#Seleciona a 'tabela'
colecao = db["info_action"]