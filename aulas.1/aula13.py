def saudar(nome, sobrenome):
 return nome + " " + sobrenome
# nomeados: a ordem fica livre
print(saudar(sobrenome="Lu",
     nome="Ana"))   #ana lu
# ERRADO: posicional depois
print(saudar(nome="Ana"))