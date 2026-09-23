# Cria uma função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(c):

    # Faz a conversão de Celsius para Fahrenheit
    fahrenheit = (c * 9 / 5) + 32

    # Retorna o resultado da conversão
    return fahrenheit


# Chama a função usando 25 graus Celsius
print(celsius_para_fahrenheit(25))

# Cria uma função para validar a senha
def validar_senha(senha):

    # Verifica se a senha possui 8 ou mais caracteres
    return len(senha) >= 8


# Testa uma senha com 8 caracteres
print(validar_senha("12345678"))

# Testa uma senha com menos de 8 caracteres
print(validar_senha("1234"))

# Cria uma função que recebe vários preços
def caixa(*precos):

    # Calcula o total dos preços
    total = sum(precos)

    # Encontra o item com o maior preço
    mais_caro = max(precos)

    # Calcula a média dos preços
    media = total / len(precos)

    # Retorna o total, o maior preço e a média
    return total, mais_caro, media


# Chama a função passando vários preços
print(caixa(10, 25.5, 7, 40))

# Cria uma função que recebe vários dados do aluno
def ficha_aluno(**dados):

    # Percorre cada informação recebida
    for chave, valor in dados.items():

        # Imprime uma informação por linha
        print(f"{chave}: {valor}")


# Chama a função passando os dados do aluno
ficha_aluno(nome="Carlos", idade=18, nota=8.5, turma="A")

# Cria uma função para somar dois números
def somar(a, b):

    # Retorna a soma dos números
    return a + b


# Cria uma função para multiplicar dois números
def multiplicar(a, b):

    # Retorna a multiplicação dos números
    return a * b


# Cria uma função para calcular a média de dois números
def media(a, b):

    # Retorna a média dos dois números
    return (a + b) / 2

# Cria uma função para adicionar um item sem modificar a lista original
def adicionar_item(lista, item):

    # Cria uma cópia da lista original
    nova_lista = lista.copy()

    # Adiciona o novo item somente na cópia
    nova_lista.append(item)

    # Retorna a nova lista
    return nova_lista


# Cria uma lista original de notas
notas = [7, 8, 9]

# Cria uma nova lista adicionando a nota 10
resultado = adicionar_item(notas, 10)

# Mostra a nova lista
print(resultado)

# Mostra a lista original, que continua igual
print(notas)

