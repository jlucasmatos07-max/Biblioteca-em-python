#livro = {"titulo": "titulo de livro", "autor": "autor do livro", "ano": 2001}
#print(livro)
#print(livro["titulo"])

acervo = []
livro = {"titulo": "", "autor": "", "ano":0}

for i in range(2):
    livro["titulo"] = input("digite o nome do livro: ")
    livro["autor"] = input("digite o nome do autor: ")
    livro["ano"] = int(input("digite o ano do livro: "))
    acervo.append(livro.copy()) # - essa linha nao sobrescreve os dados armazenados e funciona como esperado
    #acervo.append(livro) - essa linha sobrescreve os dados armazenados
print(acervo)

for livro in acervo:
    print(livro["titulo"], " - ", livro["autor"])
    #print(f"titulo: {livro['titulo']} - {livro['autor']}")

procurado = input("digite o nome do livro que deseja procurar: ")
encontrado = None

for  livro in acervo:
    if livro["titulo"] == procurado:
        encontrado = livro
        break

if encontrado:
    print(f"titulo: {encontrado['titulo']} - {encontrado['autor']}")
else:
    print("livro não encontrado")

livro = {"titulo": "", "autor": ""}
print(livro.get("ano", "ano não informado."))
