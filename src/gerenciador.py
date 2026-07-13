class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = {}
        self.id_atual = 1

    def criar_tarefa(self, titulo, prioridade="Média"):
        if not titulo:
            raise ValueError("O título da tarefa não pode ser vazio.")
        
        tarefa = {
            "id": self.id_atual,
            "titulo": titulo,
            "prioridade": prioridade,
            "status": "A Fazer",
            "alerta_atraso": False  # Linha da mudança de escopo solicitada pelo cliente
        }
        self.tarefas[self.id_atual] = tarefa
        self.id_atual += 1
        return tarefa

    def listar_tarefas(self):
        return list(self.tarefas.values())

    def atualizar_status(self, id_tarefa, novo_status):
        if id_tarefa in self.tarefas:
            self.tarefas[id_tarefa]["status"] = novo_status
            return self.tarefas[id_tarefa]
        return None

    def deletar_tarefa(self, id_tarefa):
        if id_tarefa in self.tarefas:
            return self.tarefas.pop(id_tarefa)
        return None