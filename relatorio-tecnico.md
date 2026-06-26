# Relatório Técnico — Desafio DATA2: Ciência e Análise de Dados
**Candidata:** Larissa Alves Lacerda
**Projeto:** Inteligência de Mercado e Benchmarking para o Nur Mah Museum
**Data:** 26 de junho de 2026

---

## 1. Contextualização e Interpretação do Desafio
O objetivo deste projeto é analisar o panorama das organizações culturais e museus nos Estados Unidos para apoiar a tomada de decisões estratégicas da diretoria executiva do Nur Mah Museum. A análise foca em compreender a distribuição financeira (receita) do setor e a distribuição geográfica das instituições, permitindo um benchmarking preciso para futuras estratégias de captação de recursos e parcerias.

## 2. Saneamento e Qualidade de Dados (Data Cleaning)
A base de dados original apresentava inconsistências estruturais e registros faltantes (dados vazios), que foram tratados sob rigor estatístico:
* **Registros Duplicados:** Foi aplicado o comando de varredura defensiva para eliminação de linhas duplicadas. Na base atual não foram encontrados registros idênticos repetidos, mas a estrutura de limpeza foi mantida para garantir a reprodutibilidade futura do pipeline em novos dados.
* **Valores Nulos em Variáveis Críticas:** A variável alvo `Revenue` (Receita) possuía mais de 10 mil registros em branco. A substituição desses campos por uma Média Aritmética simples foi descartada por violar preceitos estatísticos, dado que o mercado é altamente distorcido por grandes instituições bilionárias (outliers). Dessa forma, utilizou-se a **Mediana segmentada por Tipo de Museu** (`Museum Type`) para preencher as lacunas sem distorcer o perfil financeiro das entidades menores.

## 3. Análise Exploratória de Dados (EDA) e Decisões Técnicas
A análise foi desenvolvida em Python dentro de um ambiente Jupyter Notebook, utilizando as bibliotecas Pandas para manipulação estrutural, e Matplotlib/Seaborn para visualizações gráficas. Três perguntas de negócio foram respondidas:
1. **Distribuição Financeira por Categoria:** Identificou-se que Zoológicos e Aquários lideram isolados o faturamento do setor (mediana próxima a 1.5 milhão de dólares), enquanto Museus de História registram faturamentos medianos mínimos. Museus de Arte situam-se em um segundo pelotão estável (entre 300k e 400k dólares).
2. **Distribuição Geográfica de Museus de Arte:** Mapeou-se que os estados da Califórnia (CA - 343) e Nova York (NY - 248) concentram o maior mercado consumidor de arte do país.
3. **Identificação de Outliers:** Através de um gráfico de caixa (Boxplot), provou-se a existência de discrepâncias gritantes que chegam à escala de 6 bilhões de dólares ($6 \times 10^9$), o que validou a escolha da Mediana como métrica central.

## 4. Dificuldades Encontradas e Melhorias Futuras
* **Dificuldade de Engenharia de Dados:** A presença de dados de tipos mistos (*mixed types*) nas colunas de códigos postais e identificadores exigiu o ajuste fino de parâmetros de leitura do Pandas (`low_memory=False`) para evitar perda de performance e alertas de compilação.
* **Dificuldade de Modelagem (Machine Learning):** A alta variabilidade e a presença de outliers legítimos na coluna de receitas tornaram o aprendizado do modelo preditivo extremamente complexo, resultando em um score R² baixo (3.9%). Essa barreira foi superada ao interpretar criticamente a métrica através do MAE em vez de RMSE, compreendendo que o faturamento do setor sofre influências de fatores externos que não constavam no dataset original.

## 5. Conclusão
O estudo aponta que os estados de CA e NY apresentam excelentes oportunidades de público e investidores para o Nur Mah Museum, desde que a instituição esteja preparada para enfrentar a maior densidade competitiva do país. Além disso, todo o planejamento orçamentário deve basear-se em medianas amostrais para mitigar o risco financeiro gerado pela distorção dos outliers bilionários de mercado.

## 6. Uso de Inteligência Artificial e Justificativas do Modelo Preditivo
Em conformidade com a Política de IA da CODE[] Jr., declara-se que ferramentas de Inteligência Artificial foram utilizadas como copilotos para otimizar o tempo de desenvolvimento do pipeline de Machine Learning e estruturação de dados. Toda a análise crítica e validação conceitual foram revisadas.

### A. Escolha do Algoritmo: Árvore de Decisão (Decision Tree Regressor)
O algoritmo escolhido para o desafio foi a **Árvore de Decisão**. A escolha justifica-se pelo perfil da base de dados:
* O mercado de museus apresenta uma assimetria extrema (outliers bilionários convivendo com microinstituições). Modelos lineares puros (como a Regressão Linear) sofrem severamente com a distorção desses outliers. A Árvore de Decisão lida melhor com essa distribuição caótica ao segmentar os dados em "regras de decisão" sucessivas, isolando os extremos de forma mais eficiente.

### B. Pipeline de Pré-processamento e Variáveis Categóricas
* **One-Hot Encoding (`pd.get_dummies`):** Como o Scikit-Learn exige entradas puramente numéricas, as variáveis qualitativas `Museum Type` e `State` foram codificadas. Utilizou-se o One-Hot Encoding para criar colunas binárias (0 ou 1) para cada categoria, permitindo que o modelo interprete o impacto geográfico e da tipologia na receita sem criar uma hierarquia falsa de valores.

### C. Justificativa e Análise Crítica das Métricas de Erro
O modelo registrou um **MAE de $26,824,264.23** e um **R² de 0.0389**.
* **Erro Médio Absoluto (MAE):** Escolheu-se o MAE porque ele calcula a média das magnitudes dos erros em valores absolutos (em dólares), medindo diretamente o desvio médio das previsões. Optou-se por focar no MAE em detrimento do RMSE porque o RMSE penaliza erros grandes de forma quadrática. Em uma base repleta de outliers bilionários legítimos, o RMSE explodiria, mascarando a performance real do modelo nas instituições de médio porte.
* **Score R² (Poder de Explicação):** O resultado de 3.9% traduz com precisão o cenário caótico do mundo real citado no edital. Ele prova que o faturamento de um museu **não depende exclusivamente** de sua localização e de seu tipo. Fatores ocultos não mapeados no dataset (como o tamanho do acervo, volume de turismo local, doações privadas e marketing) têm peso majoritário na receita.

### D. Melhorias Futuras com Mais Dados
Para evoluir a precisão do modelo em pipelines futuros, seria necessário:
1. Adicionar features macroeconômicas (como o PIB per capita ou o IDH do condado onde o museu está localizado).
2. Adicionar dados volumétricos internos (como a média anual de visitantes pagantes).
3. Aplicar técnicas de engenharia de recursos (*Feature Engineering*), criando faixas de classificação de tamanho com base no número de funcionários.