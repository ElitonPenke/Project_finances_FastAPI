#cORAÇÃO EM IS DO SISITEMA


from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates  #rendezia o HTML

from fastapi.staticfiles import StaticFiles #entrega certinho o CSS, JavaScript ....

#meu backend em si 
from app.scraper.scraper import coletar_dados

#minha tabel do MongoBD
from app.database.mongo import colecao


#Parte inicial chamanda a aplicação----------------------------------------------------------

#Coloca meu 'servidor' a aplicação em si dentro de uma variavel
app = FastAPI() 

# mount é para minha aplicaão web conseguir acessar a parta 'static' o qual tem mue CSS
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Aqui ele conecta o HTML com o PY
templates = Jinja2Templates(directory="app/templates")


#Parte aonde criamos as ROTAS(pegar e enviar dados)------------------------------------------

#tras a plicaçõa o o GET é de trazer a informação
@app.get("/")

#função aonde ele roda quando o user entra no site e chama o HTML dinamico
def pagina_web (request: Request):

    #vai retornar o HTML que definimos acima 
    return templates.TemplateResponse(
        {"request": request},  #aqui seria as requisição que o user faz ao entrar, tp cookies, a url, o HTTP e etc
        "index.html"
    )

#Rota aonde ele vai pegar os dados do HTML, pelo forms com o action="/buscar" method="post"
@app.post("/buscar") #precisa ser o mesmo nome do HTML

def buscar(
    request:Request, #aqui seria as requisição que o user faz ao entrar, tp cookies, a url, o HTTP e etc
    acao:str=Form(...) #aqui no caso, vai recer so uma variavel e o (...) é para o campo ser obrigatio para roda
    
):
    
#ele chama a meu python scraper com o parametro acao que pegou aqui no HTML
    
    dados_do_banco=coletar_dados(acao) #vai retornar os dados que eu consegui no meu web scraping

#aqui vou pegar esses dados do meu scrap e salvar no meu banco de dados na tabela colecao
    colecao.delete_many({})
    colecao.insert_one(dados_do_banco)
    
    #vai retornar com a ação de ir para outra pagina HTML com as informações 'dados'
    return templates.TemplateResponse(
        request=request,
        name="index_2.html",
        context={"dados": dados_do_banco}  # <--- É AQUI QUE OS SEUS DADOS ENTRAM AGORA!
    )
    
    
    
#ligar o server  -->cd ..<-- -->uvicorn main:app --reload<--