import streamlit as st
import pandas as pd


# Função para carregar os dados do Excel
def load_data():
    return pd.read_excel('datasets/Pasta1.xlsx', index_col=0)

# Verifica se os dados já estão no session_state. Se não, carrega o Excel.
if 'data' not in st.session_state:
    st.session_state['data'] = load_data()

# Função para atualizar os dados
def update_data():
    st.session_state['data'] = load_data()

# Botão para atualizar os dados
if st.button('Atualizar dados'):
    update_data()

df_data = st.session_state['data']
# Verifica se a coluna 'nome_personagem' existe no DataFrame
if 'nome_personagem' in df_data.columns:
    personagens = df_data['nome_personagem'].value_counts().index
    personagem = st.sidebar.selectbox("Escolha o personagem", personagens)

    # Filtra os dados para o personagem selecionado
    df_personagem = df_data[df_data['nome_personagem'] == personagem]
    # Exibe os dados carregados (apenas para teste)
    player_stats = df_personagem.iloc[0]
    st.image(player_stats['foto'])
    st.title(player_stats['nome_personagem'])  # Título principal

    # Exibe o nome do jogador ao lado do personagem
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"**Jogador:** {player_stats['nome_jogador']}")  # Nome do jogador
    with col2:
        st.subheader(f"**Vida:** ")  # Nome do jogador
        colun1, colun2 = st.columns(2)
        with colun1:
            st.progress(int(player_stats['Vida']*10))
        with colun2:
            st.text(player_stats['Vida'])  # Nome do jogador


    # Linha de separação
    st.markdown("---")
    
    # Exibe idade, altura e sexo em uma linha
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"**Idade:** {player_stats['idade']}")
    with col2:
        st.markdown(f"**Altura:** {player_stats['altura']/100}")
    with col3:
        if player_stats['sexo'] == 'm':
            st.markdown(f"**Sexo:** Masculino")
        else:
            st.markdown(f"**Sexo:** Feminino")

    # Linha de separação
    st.markdown("---")
    
    # Exibe história e personalidade lado a lado
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown(f"**História:** {player_stats['historia']}")
    with col2:
        st.markdown(f"**Personalidade:** {player_stats['personalidade']}")
    
        # Linha de separação
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"**Carga:** ")  
        colun1, colun2 = st.columns(2)
        with colun1:
            st.progress(int(player_stats['carga']*10))
        with colun2:
            st.text(player_stats['carga'])  
    with col2:
        st.subheader(f"**Inventário:** ")  
        st.text(player_stats['inventario'])

else:
    st.error("Coluna 'nome_personagem' não encontrada nos dados.")
