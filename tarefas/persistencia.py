import json
import os

CAMINHO_DIRETORIO = os.path.join("G:", os.sep, "Arquivos", "Programacao", "Python",
                                 "Fundamentos_Python", "Modulo_1", "projeto", "tarefas_persistencia")

CAMINHO_ARQUIVO = os.path.join(CAMINHO_DIRETORIO, "tarefas.json")

os.makedirs(CAMINHO_DIRETORIO, exist_ok=True)

def carregar_tarefas():
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)
