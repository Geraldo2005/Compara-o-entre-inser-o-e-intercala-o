
import csv
import random
import time
import matplotlib.pyplot as plt

from ordenacao import insercao, intercala_sort


TAMANHOS = [5, 10, 20, 30, 50, 75, 100, 200, 500, 1000]
REPETICOES = 10


class Numero:
    comparacoes = 0

    def __init__(self, valor):
        self.valor = valor

    def __lt__(self, outro):
        Numero.comparacoes += 1
        return self.valor < outro.valor


def contar_comparacoes_sorted(lista):
    valores = [Numero(x) for x in lista]
    Numero.comparacoes = 0
    sorted(valores)
    return Numero.comparacoes


def gerar_dados():
    resultados = []

    for n in TAMANHOS:
        for repeticao in range(1, REPETICOES + 1):
            lista = [random.randint(0, 10000) for _ in range(n)]

            inicio = time.perf_counter()
            ordenada_i, comparacoes_i = insercao(lista)
            tempo_i = time.perf_counter() - inicio

            inicio = time.perf_counter()
            ordenada_m, comparacoes_m = intercala_sort(lista)
            tempo_m = time.perf_counter() - inicio

            inicio = time.perf_counter()
            ordenada_s = sorted(lista)
            tempo_s = time.perf_counter() - inicio

            comparacoes_s = contar_comparacoes_sorted(lista)

            assert ordenada_i == ordenada_m == ordenada_s

            resultados.append({
                "n": n,
                "repeticao": repeticao,
                "tempo_insercao": tempo_i,
                "tempo_intercala": tempo_m,
                "tempo_sorted": tempo_s,
                "comparacoes_insercao": comparacoes_i,
                "comparacoes_intercala": comparacoes_m,
                "comparacoes_sorted": comparacoes_s
            })

        print(f"n = {n}: medições concluídas")

    return resultados


def calcular_medias(resultados):
    medias = []

    for n in TAMANHOS:
        grupo = [r for r in resultados if r["n"] == n]

        medias.append({
            "n": n,
            "tempo_medio_insercao": sum(
                r["tempo_insercao"] for r in grupo
            ) / len(grupo),
            "tempo_medio_intercala": sum(
                r["tempo_intercala"] for r in grupo
            ) / len(grupo),
            "tempo_medio_sorted": sum(
                r["tempo_sorted"] for r in grupo
            ) / len(grupo),
            "comparacoes_insercao": sum(
                r["comparacoes_insercao"] for r in grupo
            ) / len(grupo),
            "comparacoes_intercala": sum(
                r["comparacoes_intercala"] for r in grupo
            ) / len(grupo),
            "comparacoes_sorted": sum(
                r["comparacoes_sorted"] for r in grupo
            ) / len(grupo)
        })

    return medias


def salvar_csv(resultados):
    with open("dados.csv", "w", newline="", encoding="utf-8") as arquivo:
        campos = resultados[0].keys()
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(resultados)


def gerar_graficos(medias):
    tamanhos = [r["n"] for r in medias]

    plt.figure(figsize=(10, 6))
    plt.plot(tamanhos, [r["tempo_medio_insercao"] for r in medias],
             marker="o", label="Inserção")
    plt.plot(tamanhos, [r["tempo_medio_intercala"] for r in medias],
             marker="o", label="Intercalação")
    plt.plot(tamanhos, [r["tempo_medio_sorted"] for r in medias],
             marker="o", label="sorted()")
    plt.xlabel("Tamanho da lista (n)")
    plt.ylabel("Tempo médio (segundos)")
    plt.title("Comparação dos tempos de ordenação")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("grafico_tempos.png", dpi=150)
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.plot(tamanhos, [r["comparacoes_insercao"] for r in medias],
             marker="o", label="Inserção")
    plt.plot(tamanhos, [r["comparacoes_intercala"] for r in medias],
             marker="o", label="Intercalação")
    plt.plot(tamanhos, [r["comparacoes_sorted"] for r in medias],
             marker="o", label="sorted()")
    plt.xlabel("Tamanho da lista (n)")
    plt.ylabel("Número médio de comparações")
    plt.title("Comparação do número de comparações")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("grafico_comparacoes.png", dpi=150)
    plt.close()


def main():
    resultados = gerar_dados()
    medias = calcular_medias(resultados)

    salvar_csv(resultados)
    gerar_graficos(medias)

    print("\nMedições finalizadas!")
    print("O dados.csv contém as 10 medições individuais de cada tamanho.")
    print("Os gráficos utilizam as médias das medições.")


if __name__ == "__main__":
    main()
