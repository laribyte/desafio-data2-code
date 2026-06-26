import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Nur Mah Museum - Dashboard", page_icon="🏛️", layout="wide")

st.title("Inteligência de Mercado e Benchmarking — Nur Mah Museum")
st.markdown("Este painel interativo apresenta a análise de distribuição de museus nos EUA para suporte estratégico.")

# Carregar os dados (usando cache para ficar rápido)
@st.cache_data
def carregar_dados():
    # Carrega o CSV original e aplica o saneamento rápido
    df = pd.read_csv("dados/museums.csv", low_memory=False)
    df = df.drop_duplicates()
    
    # Preenche nulos da Receita com a mediana por tipo
    medianas = df.groupby('Museum Type')['Revenue'].transform('median')
    df['Revenue'] = df['Revenue'].fillna(medianas)
    return df

try:
    df_limpo = carregar_dados()

    # FILTRO LATERAL
    st.sidebar.header("Filtros de Análise")
    estados_disponiveis = sorted(df_limpo['State (Administrative Location)'].dropna().unique())
    estado_selecionado = st.sidebar.selectbox("Selecione o Estado:", estados_disponiveis, index=estados_disponiveis.index('CA') if 'CA' in estados_disponiveis else 0)

    # Filtrar dataframe
    df_filtrado = df_limpo[df_limpo['State (Administrative Location)'] == estado_selecionado]

    # MÉTRICAS
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Museus no Estado", f"{len(df_filtrado):,}")
    col2.metric("Receita Média (Filtro)", f"${df_filtrado['Revenue'].mean():,.2f}")
    col3.metric("Receita Mediana (Filtro)", f"${df_filtrado['Revenue'].median():,.2f}")

    st.markdown("---")

    # GRÁFICOS
    col_graf1, col_graf2 = st.columns(2)

    with col_graf1:
        st.subheader(f"Tipos de Museus em {estado_selecionado}")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.countplot(data=df_filtrado, y='Museum Type', order=df_filtrado['Museum Type'].value_counts().index, palette="viridis", ax=ax)
        plt.xlabel("Quantidade")
        plt.ylabel("Tipo")
        st.pyplot(fig)

    with col_graf2:
        st.subheader("Distribuição Financeira Global por Categoria")
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        sns.boxplot(data=df_limpo, x='Revenue', y='Museum Type', palette="mako", ax=ax2)
        plt.xscale('log') # Escala logarítmica para lidar com os outliers
        plt.xlabel("Receita (Escala Log)")
        plt.ylabel("Tipo")
        st.pyplot(fig2)

except Exception as e:
    st.error(f"Erro ao carregar os dados. Certifique-se de que o arquivo 'museums.csv' está dentro da pasta 'dados/'. Detalhe: {e}")