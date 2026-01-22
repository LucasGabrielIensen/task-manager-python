import json
import os

ARQUIVO_TAREFAS = "tarefas.json"


def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)


def carregar_tarefas():
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []

    with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
