# Projeto Final GENIAL  
## Otimização de Componentes de Concreto com PSO

## Equipe

- Kalyla Lobato da Costa Pinheiro
- Valéria Oliveira Rodrigues

Este repositório apresenta a solução desenvolvida para o **Projeto Final da disciplina GENIAL**, cujo objetivo é aplicar técnicas de **Inteligência Computacional** para resolver problemas de otimização reais.

A equipe ficou responsável pelo problema de **Otimização por Enxame de Partículas (PSO)**, aplicado à **otimização da composição de concreto**, visando maximizar sua resistência à compressão aos 28 dias.

##  Contexto do Problema

O desempenho do concreto depende diretamente das proporções de seus componentes. Ajustar manualmente essas proporções é um processo custoso e sujeito a erros.

Neste projeto, utilizamos um **modelo de aprendizado de máquina (Random Forest)** previamente treinado para prever a resistência do concreto a partir das quantidades de seus componentes. O **PSO** é então aplicado para encontrar a melhor combinação possível, respeitando restrições físicas da mistura.

##  Objetivo

Maximizar a **resistência à compressão do concreto aos 28 dias**, por meio da otimização das proporções (kg/m³) de **7 componentes** da mistura, utilizando o **Algoritmo de Enxame de Partículas (PSO)**.

##  Modelagem do Problema

- **Variáveis de decisão**:  
  Quantidades (kg/m³) dos 7 componentes do concreto.
  
- **Função objetivo**:  
  Maximizar a resistência prevista pelo modelo Random Forest, com penalizações em caso de violação das restrições.

- **Restrições**:
  - Limites mínimos e máximos para cada componente.
  - Restrições de viabilidade física da mistura.

##  Algoritmo Utilizado

- **Método**: Particle Swarm Optimization (PSO)
- **Representação da partícula**: vetor com as proporções dos componentes
- **Critério de parada**: número máximo de iterações
- **Avaliação**: função objetivo baseada no modelo preditivo

##  Análise Experimental

Conforme solicitado no enunciado do projeto:

- O algoritmo PSO foi executado **pelo menos 5 vezes**.
- Foram extraídas as seguintes métricas:
  - Melhor solução
  - Pior solução
  - Média
  - Desvio padrão
  - Tempo médio de execução
- Foi gerado o **gráfico de convergência**, acompanhado de análise interpretativa dos resultados.


##  Como Executar o Projeto

- Clone o repositório:
```bash
git clone <https://github.com/Kalyla-Pinheiro/projeto_pso_equipe_on-a.git>
cd pso-concreto
```

- Instale as dependências:
```
pip install -r requirements.txt
```

- Execute o notebook:
```
jupyter notebook notebooks/Projeto_pso_final.ipynb
```

## Dependências

As dependências do projeto estão descritas no arquivo requirements.txt.

## Estrutura do Repositório

```txt
pso-concreto/
│
├── data/
│   ├── concrete.csv
│   └── modelo.pkl
│
├── src/
│   ├── pso.py
│   ├── objective.py
│   ├── constraints.py
│   └── utils.py
│
├── results/
│   ├── execucoes.csv
│   ├── estatisticas.csv
│   ├── melhor_composicao.json
│   └── grafico_convergencia.png
│
├── notebooks/
│   └── Projeto_pso_final.ipynb
│
├── requirements.txt
├── README.md
```

## Considerações Finais

Neste projeto, foi aplicado o algoritmo de Otimização por Enxame de Partículas (PSO) para maximizar a resistência à compressão do concreto aos 28 dias, utilizando um modelo Random Forest pré-treinado como função avaliadora. A função objetivo J(x), com penalização baseada na soma dos componentes em relação ao valor médio 𝑀, garantiu que as soluções permanecessem fisicamente plausíveis.

Os resultados das cinco execuções do PSO apresentaram boa estabilidade e baixo desvio, indicando o bom funcionamento do método. As curvas de convergência mostraram rápida evolução nas primeiras iterações e posterior estabilização. A composição ótima encontrada apresentou alta resistência prevista e coerência com práticas usuais de dosagem de concreto.

Como limitações, destaca-se a dependência do modelo preditivo e a ausência de validação experimental.


## Referências

- GENIAL – Projeto Final
- Notebook oficial do problema PSO
- Literatura sobre Particle Swarm Optimization


