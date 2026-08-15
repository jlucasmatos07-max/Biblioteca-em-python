#acervo.py — só o que mexe nos dados, nenhum inputn nenhum menu

def cadastrar(acervo, titulo, autor, ano):
    livro = {"titulo": titulo, "autor": autor, "ano": ano}
    acervo.append(livro)

def buscar(acervo, titulo):
    for livro in acervo:
        if livro["titulo"] == titulo:
            return livro #devolve o livro, nao imprime
    return None #percorreu tudo e não achou, devolve None

if __name__ == "__main__":
    #so roda se voce executar esse arquivo diretamente, nao se for importado
    teste = []
    cadastrar(teste, "O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
    print(buscar(teste, "O Senhor dos Anéis"))
    print(buscar(teste, "nao existe"))
