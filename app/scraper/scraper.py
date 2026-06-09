import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

#Mascara para enganhar proteção do site em si
headers = {
    'User-Agent': 'Mozilla/5.0'
}

#def que pega os dados via web scraping
def coletar_dados(action):

    #Cria o dicionario
    info_action = {}

    dados_brutos={}

    url_site = (
        'https://www.fundamentus.com.br/detalhes.php?papel='
        + action
    )
    
    #Manda o pedido HTTP
    pag = requests.get(
        url_site,
        headers=headers
    )

    #Tranforma o HTML para um object Py
    soup = BeautifulSoup(
        pag.content,
        'html.parser'
    )

    #Bloco HTML aonde todas as informações estão 
    tabelas = soup.find_all(
        'table',
        class_='w728'
    )

    #Loop para entrar em todas as tabelas HTML 
    for tabela in tabelas:

        #Pega todas as linhas dentro da tabela
        linhas = tabela.find_all('tr')

        #Pega cada linha especifica e encontra os marcadores label e dat aonde estão o conteudo de fato
        for linha in linhas:

            #Aqui usamos o 're' para pegar todos que contem dentro a palavra 'label', tp um %label% de SQL
            label = linha.find(
                'td',
                class_=re.compile('label')
            )

            data = linha.find(
                'td',
                class_=re.compile('data')
            )

            #Verifica se não tem nenhum vazio, pois a 'label' tem titulo, para evitar isso e pega so que tem correspondencia
            if label and data:

                nome = label.text.strip()
                valor = data.text.strip()

                #Aqui ele pega o dicionario e vai adicionando a chave e o valor para dentro
                dados_brutos[nome] = valor
    
    for chave, valor in dados_brutos.items():

        nova_chave = (
            chave
            .replace("?", "")      
            .strip()               
            .lower()              
            .replace(" ", "_")    
        )

        
        # adiciona no novo dicionario
        info_action[nova_chave] = valor

    
    return info_action