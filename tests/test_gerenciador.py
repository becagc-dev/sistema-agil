import pytest
from src.gerenciador import GerenciadorTarefas

def test_criar_tarefa_sucesso():
    gerenciador = GerenciadorTarefas()
    tarefa = gerenciador.criar_tarefa("Testar o pipeline", "Verificar se o GitHub Actions funciona")
    assert tarefa["nome"] == "Testar o pipeline"
    assert tarefa["concluida"] is False
    assert tarefa["prioridade"] == "Média"  # Valor padrão antigo configurado

def test_criar_tarefa_sem_nome():
    gerenciador = GerenciadorTarefas()
    with pytest.raises(ValueError, match="O nome da tarefa não pode ser vazio."):
        gerenciador.criar_tarefa("")

# --- NOVO TESTE DA MUDANÇA DE ESCOPO ---
def test_criar_tarefa_com_prioridade():
    gerenciador = GerenciadorTarefas()
    tarefa = gerenciador.criar_tarefa("Entregar carga expressa", "Urgente", prioridade="Alta")
    assert tarefa["prioridade"] == "Alta"