# Challenge CODE[] 2026.2 — Trilha de Ciência de Dados & Inteligência Analítica

## Projeto: Inteligência de Mercado e Benchmarking para o Nur Mah Museum

Este repositório contém a resolução do **Desafio DATA2** do processo de Onboarding Técnico da CODE[] Jr.. O objetivo do projeto é realizar um estudo analítico sobre o panorama das organizações culturais e museus nos Estados Unidos para fundamentar as próximas decisões estratégicas de captação de recursos e parcerias da diretoria executiva do **Nur Mah Museum**.

## Tecnologias Utilizadas

O projeto foi desenvolvido inteiramente em **Python** utilizando o ambiente do **Jupyter Notebook**, baseando-se nas seguintes bibliotecas:
* **Pandas:** Para o carregamento, manipulação estrutural e saneamento da base de dados.
* **Matplotlib & Seaborn:** Para a construção de visualizações gráficas e análise de outliers.

## Estrutura do Repositório

O projeto está organizado na seguinte estrutura de arquivos, seguindo as boas práticas de kebab-case indicadas no manual:

```text
desafio-data2-code/
├── .gitignore            # Filtro para impedir o envio de arquivos pesados ao GitHub
├── README.md             # Documentação principal com instruções de execução
├── analise_museus.ipynb  # Jupyter Notebook com o pipeline de dados e gráficos salvos
└── dados/                # Diretório local contendo a base de dados (ignorado pelo Git)
```

**Resumo do Pipeline Desenvolvido:**

1. Saneamento e Qualidade de Dados (Data Cleaning)
Registros Duplicados: Aplicação de rotina defensiva para remoção de linhas idênticas duplicadas.

Tratamento de Nulos na Variável (Revenue): Identificação de mais de 10 mil campos vazios na coluna de receita. Os dados foram tratados e preenchidos utilizando a Mediana segmentada por categoria de museu, justificando-se pela forte presença de outliers bilionários que inviabilizariam o uso da Média Aritmética simples.

2. Análise Exploratória de Dados (EDA)
O notebook responde de forma visual e textual às três dores de negócio obrigatórias:

Distribuição Financeira: Comparação de receitas medianas por tipologia de museu (onde Zoológicos e Aquários lideram e Museus de História ocupam a base do mercado).

Distribuição Geográfica: Mapeamento dos 5 estados com maior densidade de Museus de Arte, evidenciando a liderança da Califórnia (CA) e Nova York (NY).

Identificação de Outliers: Construção de um gráfico de caixa (Boxplot) comprovando a assimetria do mercado com instituições que atingem o patamar de 6 bilhões de dólares.

**Como Executar o Projeto Localmente:**

Para reproduzir a análise no seu computador, certifique-se de ter o Python instalado e siga o passo a passo abaixo:

1. Clonar o Repositório:

```bash
git clone -b feature/code-challenge [https://github.com/laribyte/desafio-data2-code.git](https://github.com/laribyte/desafio-data2-code.git)
cd desafio-data2-code
```

2. Instalar as Dependências Obrigatórias:
```bash
pip install pandas matplotlib seaborn notebook
```
3. Baixar o Dataset:

Baixe o arquivo museums.csv diretamente do Kaggle - Museum Directory Dataset.

Crie uma pasta chamada dados na raiz do projeto e mova o arquivo extraído para lá.

4. Abrir o Jupyter Notebook:
jupyter notebook

Abra o arquivo analise_museus.ipynb e execute as células sequencialmente para visualizar os códigos e gráficos gerados.

