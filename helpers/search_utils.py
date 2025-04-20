# helpers/search_utils.py

import datetime
from typing import List

# Exemplo de mock para simular busca real (depois pode ser substituído por scraping com requests/selenium)
def buscar_licitacoes_ultimos_15_dias(palavras_chave: List[str]):
    hoje = datetime.date.today()
    data_limite = hoje - datetime.timedelta(days=15)

    # Simula resultados encontrados
    resultados_mock = [
        {
            "numero_edital": "PE 90.015_25",
            "orgao": "PREFEITURA DE ITUMBIARA GO",
            "data_pregao": hoje.strftime("%Y-%m-%d"),
            "hora": "09:00",
            "portal": "www.licitacoes-e.com.br",
            "link_edital": "https://www.licitacoes-e.com.br/edital1234",
            "palavras_encontradas": ["kit cirúrgico", "papel grau cirúrgico"]
        },
        {
            "numero_edital": "PE 90.002_25",
            "orgao": "HOSPITAL GERAL DE CURITIBA PR",
            "data_pregao": (hoje + datetime.timedelta(days=3)).strftime("%Y-%m-%d"),
            "hora": "14:00",
            "portal": "www.portaldecompraspublicas.com.br",
            "link_edital": "https://www.portaldecompraspublicas.com.br/edital5678",
            "palavras_encontradas": ["avental cirúrgico"]
        }
    ]

    return resultados_mock
