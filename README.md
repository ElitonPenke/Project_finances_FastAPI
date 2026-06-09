# Web Scraper Financeiro

Aplicação que extrai dados de ações da bolsa brasileira do site Fundamentus, processa os dados e os armazena no MongoDB.

## O Projeto

- 🔍 Busca dados de ações pelo código (VALE3, PETR4, etc)
- 📊 Extrai informações do site Fundamentus
- 💾 Salva os dados no MongoDB
- 🌐 Exibe os resultados em uma página web dinâmica

## Stack de Tecnologias

- **FastAPI** - Framework web
- **BeautifulSoup** - Web scraping
- **MongoDB** - Banco de dados
- **Jinja2** - Templates HTML

## Estrutura

```
├── app/
│   ├── static/              # CSS, JS
│   ├── templates/           # HTML (index.html, index_2.html)
│   ├── scraper/scraper.py   # Web scraping
│   └── database/mongo.py    # MongoDB
├── main.py                  # Aplicação principal
└── requirements.txt
```


## Referências

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Fundamentus](https://www.fundamentus.com.br/)
