import psycopg

conexao = psycopg.connect(
    host="seu_host",
    port=5432,
    dbname="nome_do_banco",
    user="seu_usuario",
    password="sua_senha"
)

print("Conectado ao PostgreSQL!")


