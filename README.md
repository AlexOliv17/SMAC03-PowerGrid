# Conectividade e Estrutura em Redes Elétricas com Grafos 🌐
**SMAC03 - GRAFOS**

Este projeto representa um caso de estudo de Grafos, com o objetivo de analisar e aprimorar a robustez estrutural de uma rede de distribuição elétrica real utilizando a Teoria dos Grafos como ferramenta fundamental.

**Instituição:** Univerisidade Federal de Itajubá (UNIFEI) - Instituto de Matemática e Computação (IMC)<br>
**Disciplina:** SMAC03 - GRAFOS <br>
**Docente:** Prof. Rafael Frinhani<br>
**Semestre:** 2º Semestre de 2025


## Integrantes

| Nome | Matrícula | Papel/Contribuições |
| :--- | :--- | :--- |
| Alex de Oliveira Alves | 2024007996 | Estudo do Dataset, Solução Proposta, Implementação e disponibilização dos códigos, Resumo de dados coletados para reunião com professor.|
| Leonardo Siqueira Fernandes |2021001961 | Estudo de Caso, Referencial Teórico.|
| João Pedro Silva de Oliveira | 2024005140|Estudo de Caso, Análise de Resultados, Validação dos dados, Resultados, Conclusão.|
| Gabriel Barbosa Fernandes | 2023007089 | Estudo de Caso, Introdução.|

### 📝 Problemática e Diagnóstico Inicial

O estudo foi motivado por uma concessionária de energia que enfrentava interrupções localizadas e instabilidades no fornecimento não relacionadas à geração.
Após a análise do dataset completo da rede elétrica, a hipótese levantada foi a de fragilidade estrutural da topologia.

| Métrica | Valor na Rede Original |
| :--- | :--- |
| Número de vértices | 4.941 |
| Número de arestas | 6.594 |
| Grau médio | 2.66  |
| Grafo é conexo? | Sim |
| Componentes conectadas | 1  |

O diagnóstico aprofundado revelou:<br>
**Elevada Criticidade:** Cerca de **25% dos vértices** foram identificados como vértices de alta criticidade.<br>
**Pontos de Falha:** Foram detectadas **1611 arestas-ponte** (bridges), que, se removidas, fragmentariam o sistema.<br>
**Concentração de Fluxo:** A alta Centralidade de Intermediação em alguns vértices demonstrava uma topologia excessivamente dependente.<br>

### 💡 Solução Proposta: Estratégias Algorítmicas

Com base nas vulnerabilidades, foram desenvolvidos três algoritmos em Python utilizando a biblioteca `networkx` para aumentar a robustez da topologia.

| Algoritmo | Objetivo | Estratégia |
| :--- | :--- | :--- |
| **Bypass para Vértices Críticos** | Reduzir a dependência estrutural em nós. | Cria conexões diretas entre vizinhos de vértices altamente críticos. |
| **Redundância para Arestas-Ponte** | Aumentar a redundância local. | Cria novas conexões entre vizinhos dos vértices extremos de cada aresta-ponte. |
| **Augmentação Gulosa** | Melhorar a distribuição de conectividade. | Adiciona arestas entre pares de vértices com grande proximidade estrutural, mas sem ligação direta, reduzindo o congestionamento. |


## 💻 Como Rodar o Projeto

### 1° passo:
👉 Clone o repositório, onde o ambiente ja está preparado para uso.<br>
### 2° passo:
👉 Colete os dados do dataset original (powergrid.edgelist.txt) para comparação, usando os scripts "InfosBasicas.py" e "AnaliseCritica.py".<br>
### 3° passo:
👉 Você possui a possibilidade de realizar diversos tipos de testes, como:<br>
> 1. Teste unitário em cada algorítmo: Entrando com o dataset original, gera-se um dataset de saída para cada algorítmo. Pegue o dataset gerado e extraia os dados usando os scripts citados acima("InfosBasicas.py" e "AnaliseCritica.py"), compare os resultados.<br>
> 2. Testes isolando somente um algorítmo: Segue a mesma lógica do 1° caso. A diferença é que você entrará no 2° algorítmo aplicado com o dataset de saída gerado no 1° algorítmo.<br>
> 3. Teste completo: Inicie com dataset original em algum algorítmo de sua escolha, o dataset gerado na saída deve ser o de entrada do próximo. Ao final, na extração dos dados do ultimo dataset gerado todas as modificações dos 3 algorítmos estarão presentes.<br>

### 📥 Requisitos e Dependências

• Python da versão 3.10 ou mais;<br>
• Libs: NetWorkx e igraph:
```bash
pip install networkx igraph
