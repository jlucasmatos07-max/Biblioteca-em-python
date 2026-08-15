from acervo import cadastrar, buscar

livros = []

titulo = input("titulo: ")
autor = input("autor: ")
ano = int(input("ano: "))
cadastrar(livros, titulo, autor, ano) #o input ficou aqui, fora da função

achado = buscar(livros, input("buscar: "))
if achado:
    print(achado["autor"])
else:
    print("não está no acervo")