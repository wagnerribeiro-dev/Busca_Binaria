def busca_binaria(lista, busca):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        chute = lista[meio]
        if chute == busca:
            return meio
        if chute > busca:
            fim = meio - 1
        else:
            inicio = meio + 1
    return None


minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
busca = int(input('Digite o número e descrubra a posição na lista: '))
print("Posição do Elemento", busca_binaria(minha_lista, busca))
