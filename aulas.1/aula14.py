def criar(nome, ativo=True):
    if ativo:
        s = "Disponível"
    else:
        s = "Esgotado"

    return nome + " - " + s


print(criar("Caneta"))        # Caneta - Disponível
print(criar("Caneta", False)) # Caneta - Esgotado