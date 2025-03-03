import streamlit as st
import psycopg2
import os
import pandas as pd
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

# Configuração da página
st.set_page_config(
    page_title="Olá Mundo com Streamlit e PostgreSQL",
    page_icon="👋",
)

# Título da aplicação
st.title("👋 Olá Mundo!")
st.write("Bem-vindo à minha aplicação Streamlit conectada ao PostgreSQL.")

# Função para conectar ao banco de dados
def conectar_db():
    try:
        conn = psycopg2.connect(
            host="db",  # Nome do serviço no docker-compose
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return conn
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para criar uma tabela de exemplo se não existir
def inicializar_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS mensagens (
            id SERIAL PRIMARY KEY,
            texto VARCHAR(255) NOT NULL,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        # Inserir alguns dados de exemplo se a tabela estiver vazia
        cur.execute("SELECT COUNT(*) FROM mensagens")
        if cur.fetchone()[0] == 0:
            cur.execute("""
            INSERT INTO mensagens (texto) VALUES 
            ('Primeira mensagem do banco de dados!'),
            ('Olá do PostgreSQL!'),
            ('Streamlit + PostgreSQL = ❤️')
            """)
        
        conn.commit()

# Tenta conectar ao banco de dados
conn = conectar_db()

if conn:
    st.success("Conexão com o banco de dados estabelecida com sucesso!")
    
    # Inicializa o banco de dados
    inicializar_db(conn)
    
    # Exibe os dados do banco
    with conn.cursor() as cur:
        cur.execute("SELECT id, texto, data_criacao FROM mensagens")
        resultados = cur.fetchall()
        
        # Converte para DataFrame do pandas para melhor visualização
        df = pd.DataFrame(resultados, columns=["ID", "Mensagem", "Data de Criação"])
        
        st.subheader("Mensagens do Banco de Dados:")
        st.dataframe(df)
    
    # Fechar a conexão
    conn.close()
else:
    st.warning("Execute a aplicação com Docker Compose para conectar ao banco de dados PostgreSQL.") 