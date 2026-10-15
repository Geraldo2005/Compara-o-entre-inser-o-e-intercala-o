
from ordenacao import insercao, intercala_sort


def testar_ordenacao():
    casos = [
        [],
        [5],
        [3, 3, 3, 3],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [8, 2, 6, 1, 9, 3],
        [-5, 0, 4, -2, 1]
    ]

    for lista in casos:
        esperado = sorted(lista)

        resultado_insercao, comp_insercao = insercao(lista)
        resultado_intercala, comp_intercala = intercala_sort(lista)

        assert resultado_insercao == esperado
        assert resultado_intercala == esperado

        print("Lista original:", lista)
        print("Inserção:", resultado_insercao)
        print("Comparações:", comp_insercao)
        print("Intercalação:", resultado_intercala)
        print("Comparações:", comp_intercala)
        print("Teste aprovado!\n")


if __name__ == "__main__":
    testar_ordenacao()
