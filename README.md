Lenovo Laptops Web Scraper
Este projeto é um web scraper que coleta dados dos notebooks Lenovo disponíveis em Lenovo Brasil. Os dados coletados são exibidos em uma interface web usando Flask.

Funcionalidades
Web Scraping: Coleta informações de notebooks, incluindo título, preço, descrição e imagem.
Ordenação: Os produtos são listados do mais barato para o mais caro.
Interface Web: Os dados são exibidos em uma página HTML.
Requisitos
Python 3.x
Pip (gerenciador de pacotes do Python)
Dependências listadas no arquivo requirements.txt

Instalação
Clone este repositório.

Crie um ambiente virtual (opcional):
python -m venv venv
source venv/bin/activate  # Linux/MacOS
.\venv\Scripts\activate   # Windows

Instale as dependências: pip install -r requirements.txt

Execute:
Inicie o servidor Flask: python app.py

Acesse a aplicação:
Abra o navegador e vá para http://127.0.0.1:5000/.

Problemas Comuns:
Erro ModuleNotFoundError: Certifique-se de que as dependências estão instaladas corretamente.
Página não exibe dados: Verifique o console para possíveis erros de scraping.
