import streamlit as st
import pandas as pd
from pages.players import update_data
# Armazenando o usuário e a senha em variáveis
user = "usuario"
password = "senha123"
def main():
    # Carregando o arquivo Excel
    file_path = 'datasets/Pasta1.xlsx'
    df = pd.read_excel(file_path)
    df.columns = [
        'Jogador', 'Personagem', 'Idade', 'Altura', 'Sexo', 'História', 
        'Personalidade', 'Inventário', 'Peso/Max', 'Peso/Atual', 'Foto', 'Vida', 'Carga'
    ]
    # Exibindo a tabela ajustada e responsiva
    st.dataframe(df)

    # Opções para o usuário: Adicionar ou Editar personagem
    action = st.selectbox("Escolha uma ação", ["Adicionar Novo Personagem", "Editar Personagem Existente"])

    if action == "Adicionar Novo Personagem":
        # Formulário para adicionar novo personagem
        st.header("Adicionar Novo Personagem")
        
        jogador = st.text_input("Jogador")
        personagem = st.text_input("Personagem")
        idade = st.number_input("Idade", min_value=0)
        altura = st.number_input("Altura", min_value=0.0)
        sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
        historia = st.text_area("História")
        personalidade = st.text_area("Personalidade")
        inventario = st.text_area("Inventário")
        peso_max = st.number_input("Peso Máximo", min_value=0.0)
        peso_atual = st.number_input("Peso Atual", min_value=0.0)
        foto = st.text_input("Foto (URL ou caminho)")
        vida = st.number_input("Vida", min_value=0)
        carga = st.number_input("Carga", min_value=0)
        
        if st.button("Adicionar Personagem"):
            # Adiciona o novo personagem à tabela
            novo_personagem = {
                'Jogador': jogador,
                'Personagem': personagem,
                'Idade': idade,
                'Altura': altura,
                'Sexo': sexo,
                'História': historia,
                'Personalidade': personalidade,
                'Inventário': inventario,
                'Peso/Max': peso_max,
                'Peso/Atual': peso_atual,
                'Foto': foto,
                'Vida': vida,
                'Carga': carga
            }
            
            # Transformando o dicionário em um DataFrame de uma linha
            novo_personagem_df = pd.DataFrame([novo_personagem])

            # Concatenando o novo personagem ao DataFrame existente
            df = pd.concat([df, novo_personagem_df], ignore_index=True)
            
            # Salvar no Excel
            df.to_excel(file_path, index=False)
            st.success("Novo personagem adicionado com sucesso!")

    elif action == "Editar Personagem Existente":
        # Formulário para editar personagem
        st.header("Editar Personagem Existente")
        
        # Escolher o personagem para editar
        personagens = df['Personagem'].tolist()
        personagem_edit = st.selectbox("Escolha um personagem para editar", personagens)

        # Localizar o personagem na tabela
        personagem_data = df[df['Personagem'] == personagem_edit].iloc[0]

        jogador = st.text_input("Jogador", value=personagem_data['Jogador'])
        idade = st.number_input("Idade", min_value=0, value=personagem_data['Idade'])
        altura = st.number_input("Altura", min_value=0.0, value=float(personagem_data['Altura']))
        sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"], index=["m", "f",'Masculino','Feminino',"o","Outro"].index(personagem_data['Sexo']))
        historia = st.text_area("História", value=personagem_data['História'])
        personalidade = st.text_area("Personalidade", value=personagem_data['Personalidade'])
        inventario = st.text_area("Inventário", value=personagem_data['Inventário'])
        peso_max = st.number_input("Peso Máximo", min_value=0.0, value=float(personagem_data['Peso/Max']))
        peso_atual = st.number_input("Peso Atual", min_value=0.0, value=float(personagem_data['Peso/Atual']))
        foto = st.text_input("Foto (URL ou caminho)", value=personagem_data['Foto'])
        vida = st.number_input("Vida", min_value=0, value=personagem_data['Vida'])
        carga = st.number_input("Carga", min_value=0, value=personagem_data['Carga'])
        
        if st.button("Salvar Alterações"):
            # Atualiza o personagem na tabela
            df.loc[df['Personagem'] == personagem_edit, 'Jogador'] = jogador
            df.loc[df['Personagem'] == personagem_edit, 'Idade'] = idade
            df.loc[df['Personagem'] == personagem_edit, 'Altura'] = altura
            df.loc[df['Personagem'] == personagem_edit, 'Sexo'] = sexo
            df.loc[df['Personagem'] == personagem_edit, 'História'] = historia
            df.loc[df['Personagem'] == personagem_edit, 'Personalidade'] = personalidade
            df.loc[df['Personagem'] == personagem_edit, 'Inventário'] = inventario
            df.loc[df['Personagem'] == personagem_edit, 'Peso/Max'] = peso_max
            df.loc[df['Personagem'] == personagem_edit, 'Peso/Atual'] = peso_atual
            df.loc[df['Personagem'] == personagem_edit, 'Foto'] = foto
            df.loc[df['Personagem'] == personagem_edit, 'Vida'] = vida
            df.loc[df['Personagem'] == personagem_edit, 'Carga'] = carga
            
            # Salvar no Excel
            df.to_excel(file_path, index=False)
            st.success(f"Informações de {personagem_edit} atualizadas com sucesso!")
            update_data()

def login():
    # Campos para o usuário e a senha
    username = st.text_input("Usuário")
    pwd = st.text_input("Senha", type="password")

    # Verificando as credenciais
    if st.button("Login"):
        if username == user and pwd == password:
            st.session_state.logged_in = True
            st.success("Login bem-sucedido!")
            st.rerun()
        else:
            st.session_state.logged_in = False
            st.error("Usuário ou senha incorretos!")

# Verificando se o usuário está logado
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Exibindo a tabela somente se o usuário estiver logado
if st.session_state.logged_in:
    main()

else:
    login()
