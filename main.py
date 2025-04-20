# main.py

import datetime
from helpers.search_utils import buscar_licitacoes_ultimos_15_dias
from helpers.extract_info import extrair_detalhes_editais
from helpers.icloud_calendar import adicionar_eventos_icloud
from helpers.keywords import PALAVRAS_CHAVE
import pandas as pd
import os

# Etapa 1: Buscar licitações nos últimos 15 dias
print("[INFO] Buscando licitações...")
resultados = buscar_licitacoes_ultimos_15_dias(PALAVRAS_CHAVE)

# Etapa 2: Extrair dados relevantes dos editais
print("[INFO] Extraindo informações relevantes dos editais...")
resumos = extrair_detalhes_editais(resultados)

# Etapa 3: Salvar resultado em Excel
print("[INFO] Salvando resultados em Excel...")
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
excel_path = os.path.join(output_dir, "resultados.xlsx")
df = pd.DataFrame(resumos)
df.to_excel(excel_path, index=False)
print(f"[SUCESSO] Resultados salvos em {excel_path}")

# Etapa 4: Adicionar eventos na agenda do iCloud
print("[INFO] Enviando eventos para a agenda do iCloud...")
adicionar_eventos_icloud(resumos)
print("[SUCESSO] Eventos adicionados com sucesso!")
