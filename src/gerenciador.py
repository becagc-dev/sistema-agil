class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def criar_tarefa(self, nome, descricao="", prioridade="Média"):
        if not nome:
            raise ValueError("O nome da tarefa não pode ser vazio.")
        
        tarefa = {
            "id": len(self.tarefas) + 1,
            "nome": nome,
            "descricao": descricao,
            "prioridade": prioridade,  # Nova funcionalidade da mudança de escopo
            "concluida": False
        }
        self.tarefas.append(tarefa)
        return tarefa

    def listar_tarefas(self):
        return self.tarefas

    def atualizar_tarefa(self, id_tarefa, novos_dados):
        for tarefa in self.tarefas:
            if tarefa["id"] == id_tarefa:
                tarefa.update(novos_dados)
                return tarefa
        return None

    def excluir_tarefa(self, id_tarefa):
        for i, tarefa in enumerate(self.tarefas):
            if tarefa["id"] == id_tarefa:
                return self.tarefas.pop(i)
        return None