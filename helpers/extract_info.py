# helpers/extract_info.py

from typing import List, Dict

# Essa função cria um resumo estruturado de cada licitação com os campos desejados
def extrair_detalhes_editais(resultados: List[Dict]) -> List[Dict]:
    resumos = []
    for r in resultados:
        resumo = {
            "Nº do Edital": r["numero_edital"],
            "Órgão": r["orgao"],
            "UF": r["orgao"].split()[-1],
            "Data do Pregão": r["data_pregao"],
            "Horário": r["hora"],
            "Portal": r["portal"],
            "Link do Edital": r["link_edital"],
            "Palavras-chave encontradas": ", ".join(r["palavras_encontradas"])
        }
        resumos.append(resumo)
    return resumos

