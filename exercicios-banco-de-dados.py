import sqlite3

conexao = sqlite3.connect('banco_atividade')
cursor = conexao.cursor()

# Eliminando a tabela alunos caso ela já exista
cursor.execute('DROP TABLE IF EXISTS alunos')

# 1. Criando a tabela alunos
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

# 2. Inserindo registros de alunos
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Fábio Silva", 32, "Direito")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Fábio Silva", 32, "Direito")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Amanda Souza", 20, "Educação Física ")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Carlos Santos", 19, "Administração")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Felipe Lira", 17, "Medicina")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (6, "Marina Perez", 31, "Medicina")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (7, "Pablo Barone", 30, "Odontologia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (8, "Luís Henrique Canani", 21, "Farmácia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (9, "Brenda Silva", 22, "Direito")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (10, "Eliseu Pereira", 30, "Jornalismo")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (11, "Emanoelle Almeida", 34, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (12, "Miguel Costa", 27, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (13, "Helena Rocha", 19, "Engenharia")')

# 2. Realizando consultas básicas de seleção
# a) Selecionar todos os registros da tabela "alunos".
cursor.execute('SELECT * FROM alunos')

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dados = cursor.execute('SELECT nome, curso FROM alunos WHERE idade>20')
for alunos in dados:
    print(alunos)

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética
dados = cursor.execute('SELECT nome, curso FROM alunos WHERE curso="Engenharia" ORDER BY nome')
for alunos in dados:
    print(alunos)

# d) Contar o número total de alunos na tabela
dados = cursor.execute('SELECT COUNT(*) FROM alunos')
total_alunos = dados.fetchone()[0]
print(total_alunos)

# 4. Atualização e Remoção
# a) Atualize a idade de um aluno específico na tabela.
dados = cursor.execute('SELECT * FROM alunos')
cursor.execute('UPDATE alunos SET idade=23 WHERE nome="Helena Rocha"')    

# b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos WHERE id=2')    

# 5. Criar uma Tabela e Inserir Dados
cursor.execute('CREATE TABLE clientes(id INTEGER PRIMARY KEY, nome VARCHAR(100), idade INT, saldo REAL)')
# 5. Inserindo registros na tabela
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Cláudia Silva", 32, 500)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Fernando Silva", 32, 1300)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "Amanda Boarin", 20, 1805)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (4, "Carlos Santana", 19, 1440)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (5, "Felipe Tramontina", 17, 219)')

# 6. Consultas e Funções Agregadas
# Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')
for clientes in dados:
    print(clientes)

# b) Calcule o saldo médio dos clientes.
cursor.execute('SELECT AVG(saldo) FROM clientes')
valor_medio = cursor.fetchone()[0]
print(f'O valor médio do saldo dos clientes é {valor_medio}')

# c) Encontre o cliente com o saldo máximo.
cursor.execute('SELECT nome FROM clientes ORDER BY saldo DESC LIMIT 1')
cliente_saldo_maximo = cursor.fetchone()
print(f'Cliente com saldo máximo: {cliente_saldo_maximo}')

# d) Conte quantos clientes têm saldo acima de 1000.
dados = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo>1000')
total_clientes = dados.fetchone()[0]
print(total_clientes)

#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
dados = cursor.execute('SELECT * FROM clientes')
cursor.execute('UPDATE clientes SET saldo=1100 WHERE nome="Carlos Santana"')   

#b) Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes WHERE id=5')  

#8. Junção de Tabelas
cursor.execute('CREATE TABLE compras(id INTEGER PRIMARY KEY, cliente_id INTEGER, produto VARCHAR(100), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (1, 1, "Bolsa", 200)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (2, 2, "Sapato", 300)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (3, 3, "Calça", 245)')
# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
resultados = cursor.execute('SELECT clientes.nome as nome_cliente, compras.produto, compras.valor FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id')
for resultado in resultados:
    print(f'Cliente: {resultado[0]}, Produto: {resultado[1]}, Valor: {resultado[2]}')


conexao.commit()
conexao.close