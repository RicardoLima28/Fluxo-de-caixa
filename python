import psycopg

def conectar():
    conexao = psycopg.connect(
        host="seu_host",
        port=5432,
        dbname="nome_do_banco",
        user="seu_usuario",
        password="sua_senha"
    )

    return conexao

def fechar_conexao(conexao, cursor): #Function para Fechar conexão
    conexao.commit()
    cursor.close()
    conexao.close()

def cadastro_marca():                #Function para Cadastro de marca 
    nome = input("Digite o nome da marca: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO marca (nome) VALUES (%s)",
        (nome,)
    )

    fechar_conexao(conexao, cursor)
    print(f"Marca '{nome}' cadastrada com sucesso!")

def cadastro_categoria():              #Function para Cadastro de categoria
    nome = input("Digite a categoria: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO categoria (nome) VALUES (%s)",
        (nome,)
    )

    fechar_conexao(conexao, cursor)
    print(f"Categoria '{nome}' cadastrada com sucesso!")

def cadastro_produto():                 #Function para Cadastro de Produto
    nome = input("Insira o nome do produto: ")
    descricao = input("Adicione uma descrição ao seu produto: ")
    cod_int = input("Adicione um código interno: ")
    marca_id = input("Insira o ID da marca: ")
    categoria_id = input("Insira o ID da categoria: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO produtos (nome, descricao, cod_int, marca_id, categoria_id) VALUES (%s, %s, %s, %s, %s)",
        (nome, descricao, cod_int, marca_id, categoria_id)
    )

    fechar_conexao(conexao, cursor)
    print(f"Produto '{nome}', '{descricao}' e código interno: '{cod_int}' cadastrado com sucesso!")

def cadastro_pessoa():                     #Function para Cadastro de pessoa
    nome = input("Insira o nome da pessoa: ")
    email = input("Insira o email da pessoa: ")
    limite = 11

    while True:

        telefone = input("Insira o telefone da pessoa:")

        if telefone.isdigit() and len(telefone) == limite:
            print("Telefone válido")
            break
        elif len(telefone) != limite:
            print("Quantidade de caracteres inválido")
        else:
            print("Digite apenas números!")

    while True:

        cpf = input("Insira o cpf da pessoa: ")

        if cpf.isdigit() and len(cpf) == limite:
            print("CPF válido")
            break
        elif len(cpf) != limite:
            print("Quantidade de caracteres inválido")
        else:
            print("Digite apenas números")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO pessoas (nome, email, telefone, cpf) VALUES (%s, %s, %s, %s)",
        (nome, email, telefone, cpf)
    )

    fechar_conexao(conexao, cursor)
    print(f"'{nome}' email '{email}' telefone '{telefone}' e cpf '{cpf}' cadastrado com sucesso!")

def cadastro_preco():                       #Function para Cadastro de preço
    produtos_id = input("Insira o id do produto que vai adicionar o preço: ")
    preco_varejo = input("Insira o preço para o varejo: ")
    preco_atacado = input("Insira o preço para o atacado: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO preco (produtos_id, preco_varejo, preco_atacado) VALUES (%s, %s, %s)",
        (produtos_id, preco_varejo, preco_atacado)
    )

    fechar_conexao(conexao, cursor)
    print(f"Preço cadastrado no produto: '{produtos_id}' com valor no varejo de: '{preco_varejo}' e atacado '{preco_atacado}' com sucesso!")

def cadastro_operador():                      #Function para Cadastro de operador
    conexao = conectar()
    cursor = conexao.cursor()

    while True:
        operador = input("Insira o id da pessoa que será o operador: ")

        cursor.execute(
            "SELECT id FROM pessoas WHERE id = %s",
            (operador,)
        )

        resultado = cursor.fetchone()

        if resultado:
            print(f"Pessoa '{operador}' encontrada e poderá operar o caixa!")
            break
        else:
            print(f"Pessoa '{operador}' não encontrada!")

        fechar_conexao(conexao, cursor)

def abre_caixa():                           #Function para Abrir o caixa
    id_caixa = input("Insira o id do caixa para abrir: ")
    operador_id = input("Insira o id da pessoa que vai operar o caixa: ")
    valor_inicial = input("Insira o valor inicial do caixa: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id FROM movimentacao_caixa WHERE caixa_id = %s AND status = %s",
        (id_caixa, "ATIVO")
    )

    resultado = cursor.fetchone()

    if resultado:
        print("O caixa já está aberto!")
    else:
        cursor.execute(
            "INSERT INTO movimentacao_caixa (caixa_id, operador_id, data_abertura, status, valor_inicial) VALUES (%s, %s, CURRENT_TIMESTAMP, %s, %s)",
            (id_caixa, operador_id, "ATIVO", valor_inicial)
        )

        print(f"O caixa '{id_caixa}' foi aberto com sucesso!")

    fechar_conexao(conexao, cursor)

def fecha_caixa():                            #Function para Fechar o caixa
    id_caixa = input("Insira o id do caixa para fechar: ")
    valor_final = input("Insira o valor final do caixa: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id FROM movimentacao_caixa WHERE caixa_id = %s AND status = %s",
        (id_caixa, "ATIVO")
    )

    resultado = cursor.fetchone()

    if resultado:
        id_movimentacao = resultado[0]

        cursor.execute(
            "UPDATE movimentacao_caixa SET status = %s, data_fechamento = CURRENT_TIMESTAMP, valor_final = %s WHERE id = %s",
            ("INATIVO", valor_final, id_movimentacao)
        )

        print(f"O caixa '{id_caixa}' foi fechado com sucesso!")
    else:
        print(f"O caixa '{id_caixa}' não está aberto!")

    fechar_conexao(conexao, cursor)


def atualiza_estoque(produtos_id, quantidade, operacao):
    conexao = conectar()
    cursor = conexao.cursor()
    operacao = "-"

    if operacao == "+":
        cursor.execute(
            "UPDATE estoque SET quantidade_itens = quantidade_itens + %s WHERE produtos_id = %s",
            (quantidade, produtos_id)
        )
    elif operacao == "-":
        cursor.execute(
            "UPDATE estoque SET quantidade_itens = quantidade_itens - %s WHERE produtos_id = %s",
            (quantidade, produtos_id)
        )

    print(f"Estoque do produto '{produtos_id}' atualizado com sucesso!")

    fechar_conexao(conexao, cursor)

def editar_estoque ():
    conexao = conectar()
    cursor = conexao.cursor()

    while True:

        produto = input("Insira o código interno do produto: ")

        while True:

            cursor.execute(
                "SELECT id, nome FROM produtos WHERE cod_int = %s",
                (produto,)
            )

            resultado = cursor.fetchone()

    
            if resultado:
                produtos_id = resultado[0]
                nome_produto = resultado[1]

                cursor.execute(
                    "SELECT quantidade_itens FROM estoque WHERE produtos_id = %s",
                    (produtos_id,)
                )

                estoque_atual = cursor.fetchone()

                print(f"Produto: {nome_produto} - Quantidade atual em estoque é de: {estoque_atual[0]}")

                break

            else:
                print("Algum erro ocorreu, certifique-se de estar colocando o código certo")

        operacao = input("Digite '+' para adcionar e '-' para subtrair: ")
        quantidade = int(input("Digite a quantidade: "))

        if operacao == "+":
            cursor.execute(
                "UPDATE estoque SET quantidade_itens = quantidade_itens + %s WHERE produtos_id = %s",
                (quantidade, produtos_id)
            )
        elif operacao == "-":
            cursor.execute(
                "UPDATE estoque SET quantidade_itens = quantidade_itens - %s WHERE produtos_id = %s",
                (quantidade, produtos_id)
            )

        continuar = input("Deseja fazer mais operações? [s] para sim [n] para não: ")

        if continuar == "s" or continuar == "S":
            continue
        elif continuar == "n" or continuar == "N":
            break
        else:
            print("Digite apenas [s] para sim e [n] para não")

        fechar_conexao(conexao, cursor)

def cadastro_caixa():

    conexao = conectar()
    cursor = conexao.cursor()

    while True:
        caixa = int(input("Insira o número do caixa para cadastrar"))

        cursor.execute(
            "SELECT id FROM caixa WHERE id = %s",
            (caixa,)
        )

        resultado = cursor.fetchone()

        if resultado:
            print("Esse caixa já existe! Tente outro")
        else: 
            cursor.execute(
               "INSERT INTO caixa DEFAULT VALUES"                
                (caixa,)
            )

        cadastro_operador()

        fechar_conexao(conexao.cursor)

def cadastro_cliente():
    conexao = conectar()
    cursor = conexao.cursor()

    while True:
        existe_ou_nao = input("Esse cliente ja foi cadastrado como pessoa? ")
        if existe_ou_nao == "s" and existe_ou_nao == "S" and existe_ou_nao == "sim" and existe_ou_nao == "Sim":
            nome = input("Insira o nome já cadastrado: ")

            cursor.execute(
                "SELECT nome FROM pessoas WHERE nome = %s",
                (nome,)
            )

            resultado = cursor.fetchone()
            print("Esses cliente foi encontrado", resultado)
            if resultado:
                codigo = int(input("Insira um código para esse cliente"))
            