from .persistencia import salvar_tarefas

def adicionar_tarefa(tarefas, nome):
    tarefas.append({"tarefa": nome, "completada": False})
    salvar_tarefas(tarefas)

def atualizar_tarefa(tarefas, indice, novo_nome):
    tarefas[indice]["tarefa"] = novo_nome
    salvar_tarefas(tarefas)

def completar_tarefa(tarefas, indice):
    tarefas[indice]["completada"] = True
    salvar_tarefas(tarefas)

def deletar_completadas(tarefas):
    tarefas[:] = [t for t in tarefas if not t["completada"]]
    salvar_tarefas(tarefas)
