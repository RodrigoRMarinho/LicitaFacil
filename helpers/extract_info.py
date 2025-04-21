# helpers/extract_info.py

def extrair_detalhes_editais(resultados):
    resumos = []
    
    for resultado in resultados:
        resumo = {
            'numero_edital': resultado.get('numero_edital', 'N/A'),  # Exemplo de preenchimento
            'orgao': resultado.get('orgao', 'N/A'),
            'data': resultado.get('data', '01/01/1970'),
            'hora': resultado.get('hora', '09:00'),
            'plataforma': resultado.get('plataforma', 'Desconhecida'),
            'item_nome': resultado.get('item_nome', 'Item não especificado'),
            'descricao': resultado.get('descricao', 'Sem descrição'),
            'quantidade': resultado.get('quantidade', 0)
        }
        resumos.append(resumo)
    
    return resumos
