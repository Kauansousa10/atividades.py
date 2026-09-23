# int, float, str e tupla: imutáveis

def dobrar(numero):
    numero = numero * 2  # novo objeto
    return numero

valor = 10

print(dobrar(valor))
print(valor)

# Objetos imutáveis:
# Números, textos e tuplas

# Saída:
# 20
# 10 (intacto)

# str: "abc".upper() cria outra string
texto = "abc"
novo_texto = texto.upper()

print(novo_texto)  # ABC
print(texto)       # abc (intacto)