[![Pipeline de Integração Contínua (CI)](https://github.com/becagc-dev/sistema-agil/actions/workflows/main.yml/badge.svg)](https://github.com/becagc-dev/sistema-agil/actions/workflows/main.yml)
Sistema de Gerenciamento de Tarefas (Task Manager)
🎯 Objetivo do Projeto
Este projeto foi desenvolvido como parte de uma atividade de Engenharia de Software para a TechFlow Solutions. O objetivo é oferecer uma solução de gerenciamento de tarefas focada em agilidade, permitindo que uma startup de logística organize seu fluxo de trabalho, priorize demandas críticas e mantenha o controle de desempenho da equipe em tempo real.

🚀 Metodologia
O projeto adota o framework Kanban para a gestão do fluxo de trabalho. A organização das tarefas é realizada através do quadro GitHub Projects, estruturado nas colunas:

To Do (A Fazer): Tarefas pendentes no backlog.

In Progress (Em Progresso): Atividades em execução.

Done (Concluído): Entregas finalizadas e validadas.

🛠 Funcionalidades
CRUD de Tarefas: Criação, leitura, atualização e remoção de tarefas.

Priorização: Suporte a campos de prioridade (Alta, Média, Baixa) para identificação de urgência.

Automação: Pipeline de CI com GitHub Actions para execução de testes unitários.

🔄 Gestão de Mudanças
Durante o desenvolvimento, identificamos a necessidade de uma funcionalidade extra: a atribuição de níveis de prioridade às tarefas. Esta alteração foi incorporada ao escopo do projeto para atender às demandas de criticidade logística, demonstrando a flexibilidade e adaptabilidade da metodologia ágil aplicada.

⚙️ Como Executar
Clone o repositório:

Bash
git clone https://github.com/becagc-dev/sistema-agil.git
Instale as dependências:

Bash
pip install -r requirements.txt
Execute os testes automatizados para garantir a integridade do código:

Bash
pytest
📈 Controle de Qualidade
A qualidade do código é garantida por meio de Testes Unitários (Pytest). Cada push realizado no repositório aciona automaticamente o GitHub Actions, que compila o código e executa os testes, assegurando que novas implementações não comprometam funcionalidades existentes.

Projeto desenvolvido como parte da disciplina de Engenharia de Software - UniFECAF.
