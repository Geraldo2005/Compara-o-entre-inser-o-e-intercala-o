
def insercao(lista):
    v = lista.copy()
    comparacoes = 0

    for i in range(1, len(v)):
        chave = v[i]
        j = i - 1

        while j >= 0:
            comparacoes += 1

            if v[j] > chave:
                v[j + 1] = v[j]
                j -= 1
            else:
                break

        v[j + 1] = chave

    return v, comparacoes

def intercala(v, inicio, meio, fim):
    esquerda = v[inicio:meio]
    direita = v[meio:fim]
    i = 0
    j = 0
    k = inicio
    comparacoes = 0

    while i < len(esquerda) and j < len(direita):
        comparacoes += 1

        if esquerda[i] <= direita[j]:
            v[k] = esquerda[i]
            i += 1
        else:
            v[k] = direita[j]
            j += 1

        k += 1

    while i < len(esquerda):
        v[k] = esquerda[i]
        i += 1
        k += 1

    while j < len(direita):
        v[k] = direita[j]
        j += 1
        k += 1

    return comparacoes


def merge_sort_recursivo(v, inicio, fim):
    if fim - inicio <= 1:
        return 0

    meio = (inicio + fim) // 2

    comparacoes = merge_sort_recursivo(v, inicio, meio)
    comparacoes += merge_sort_recursivo(v, meio, fim)
    comparacoes += intercala(v, inicio, meio, fim)

    return comparacoes


def intercala_sort(lista):
    v = lista.copy()
    comparacoes = merge_sort_recursivo(v, 0, len(v))
    return v, comparacoes
