import pytest
from src.gerenciador import GerenciadorTarefas

def test_criar_tarefa_sucesso():
    gerenciador = GerenciadorTarefas()
    tarefa = gerenciador.criar_tarefa("Entregar carga na Zona Sul", "Alta")
    assert tarefa["id"] == 1
    assert tarefa["titulo"] == "Entregar carga na Zona Sul"
    assert tarefa["status"] == "A Fazer"

def test_criar_tarefa_com_titulo_vazio():
    gerenciador = GerenciadorTarefas()
    with pytest.raises(ValueError, match="O título da tarefa não pode ser vazio."):
        gerenciador.criar_tarefa("")

def test_atualizar_status_tarefa():
    gerenciador = GerenciadorTarefas()
    tarefa = gerenciador.criar_tarefa("Coleta de container no porto")
    tarefa_atualizada = gerenciador.atualizar_status(1, "Em Progresso")
    assert tarefa_atualizada["status"] == "Em Progresso"