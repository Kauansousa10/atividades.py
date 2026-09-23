def rel(titulo, *itens, fmt="txt", **extras):
    print(titulo, fmt)
    print(itens)      # tupla
    print(extras)     # dicionário


rel("Vendas", "jan", "fev", fmt="pdf", autor="Ana")