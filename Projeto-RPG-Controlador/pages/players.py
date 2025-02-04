import streamlit as st
import pandas as pd
import random

# Função para carregar os dados do Excel
def load_data():
    try:
        return pd.read_excel('datasets/Pasta1.xlsx', header=0)
    except FileNotFoundError:
        st.error("Arquivo 'Pasta1.xlsx' não encontrado. Verifique o caminho e o nome do arquivo.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
        return pd.DataFrame()

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

try:
    # Verifica se a coluna 'Personagem' existe no DataFrame
    if 'Personagem' in df_data.columns:
        personagens = df_data['Personagem'].value_counts().index
        personagem = st.sidebar.selectbox("Escolha o personagem", personagens)

        # Filtra os dados para o personagem selecionado
        df_personagem = df_data[df_data['Personagem'] == personagem]
        # Exibe os dados carregados (apenas para teste)
        player_stats = df_personagem.iloc[0]

        try:
            st.image(player_stats['Foto'])
        except Exception:
            st.warning("Imagem não disponível ou caminho inválido.")

        st.title(player_stats['Personagem'])  # Título principal

        # Exibe o nome do jogador ao lado do personagem
        col1, col2 = st.columns(2)
        with col1:
            try:
                st.subheader(f"**Jogador:** {player_stats['Jogador']}")  # Nome do jogador
            except KeyError:
                st.warning("Coluna 'Jogador' não encontrada.")
        with col2:
            st.subheader("**Vida:** ")  # Nome do jogador
            colun1, colun2 = st.columns(2)
            with colun1:
                try:
                    st.progress(int(player_stats['Vida'] * 10))
                except KeyError:
                    st.warning("Coluna 'Vida' não encontrada.")
                except ValueError:
                    st.warning("Valor inválido para 'Vida'.")
            with colun2:
                st.text(player_stats.get('Vida', 'N/A'))  # Nome do jogador

        # Linha de separação
        st.markdown("---")

        # Exibe Idade, Altura e sexo em uma linha
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"**Idade:** {player_stats.get('Idade', 'N/A')}")
        with col2:
            try:
                st.markdown(f"**Altura:** {player_stats['Altura'] / 100}")
            except KeyError:
                st.warning("Coluna 'Altura' não encontrada.")
            except TypeError:
                st.warning("Valor inválido para 'Altura'.")
        with col3:
            sexo = player_stats.get('Sexo', 'N/A')
            if sexo == 'm':
                st.markdown("**Sexo:** Masculino")
            elif sexo == 'f':
                st.markdown("**Sexo:** Feminino")
            else:
                st.markdown("**Sexo:** N/A")

        # Linha de separação
        st.markdown("---")

        # Exibe história e Personalidade lado a lado
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown(f"**História:** {player_stats.get('História', 'N/A')}")
        with col2:
            st.markdown(f"**Personalidade:** {player_stats.get('Personalidade', 'N/A')}")

        # Linha de separação
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("**Carga:** ")
            colun1, colun2 = st.columns(2)
            with colun1:
                try:
                    st.progress(int(player_stats['Carga'] * 10))
                except KeyError:
                    st.warning("Coluna 'Carga' não encontrada.")
                except ValueError:
                    st.warning("Valor inválido para 'Carga'.")
            with colun2:
                st.text(player_stats.get('Carga', 'N/A'))
        with col2:
            st.subheader("**Inventário:** ")
            st.text(player_stats.get('Inventário', 'N/A'))

    else:
        st.error("Coluna 'Personagem' não encontrada nos dados.")

    def rolar_dado(dado):
        lados = int(dado.split('d')[1])
        return random.randint(1, lados)
    dado = st.sidebar.selectbox("Escolha o tipo de dado:", ["1d4", "1d6", "1d8", "1d10", "1d12", "1d20"])
    resultado_dado = rolar_dado(dado)
    st.sidebar.write(f"Resultado da rolagem ({dado}): {resultado_dado}")
    
except Exception as e:
    st.error(f"Erro inesperado: {e}")