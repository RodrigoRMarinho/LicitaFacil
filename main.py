# main.py

from helpers.search_utils import buscar_licitacoes_ultimos_15_dias
from helpers.extract_info import extrair_detalhes_editais
from helpers.keywords import PALAVRAS_CHAVE
from helpers.icloud_calendar import autenticar_icloud, adicionar_eventos_na_agenda

import getpass
import os
import pandas as pd

# 1. Buscar licitações com base nas palavras-chave dos últimos 15 dias
print("🔎 Buscando licitações...")
resultados = buscar_licitacoes_ultimos_15_dias(PALAVRAS_CHAVE)

# 2. Extrair detalhes de interesse
print("📄 Extraindo informações relevantes dos editais...")
resumos = extrair_detalhes_editais(resultados)

# 3. Salvar resumo em Excel
os.makedirs("output", exist_ok=True)
excel_path = "output/resumo_licitacoes.xlsx"
pd.DataFrame(resumos).to_excel(excel_path, index=False)
print(f"✅ Resumo salvo em: {excel_path}")

# 4. Login na conta iCloud do usuário
print("🔐 Login no iCloud...")
usuario_icloud = input("Digite seu e-mail iCloud: ")
senha_icloud = getpass.getpass("Digite sua senha iCloud (não aparece enquanto digita): ")

icloud = autenticar_icloud(usuario_icloud, senha_icloud)

# 5. Adicionar eventos à agenda do iCloud
print("🗓️ Adicionando eventos à sua agenda iCloud...")
adicionar_eventos_na_agenda(icloud, resumos)

print("🎉 Tudo pronto! Licitações analisadas e agenda atualizada com sucesso.")

