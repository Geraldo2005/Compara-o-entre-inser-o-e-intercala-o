# Projeto de Ordenação

## Descrição

Este projeto implementa e compara dois algoritmos de ordenação: ordenação por inserção e ordenação por intercalação. Também utiliza a função `sorted()` do Python como referência de desempenho.

São realizadas medições de tempo e contagem de comparações para diferentes tamanhos de listas.

## Arquivos do projeto

- `ordenacao.py`: implementação dos algoritmos de inserção e intercalação.
- `testes.py`: testes de funcionamento dos algoritmos.
- `medir.py`: execução das medições, cálculo das médias e geração dos resultados.
- `dados.csv`: dados individuais das medições realizadas.
- `grafico_tempos.png`: gráfico dos tempos médios de execução.
- `grafico_comparacoes.png`: gráfico do número médio de comparações.
- `RELATORIO.md`: relatório com metodologia, tabelas, gráficos, análise e conclusão.

## Requisitos

- Python 3 instalado.
- Biblioteca Matplotlib para geração dos gráficos.

## Como executar

### 1. Instalar a biblioteca

No terminal do VS Code, execute:

```powershell
.\.venv\Scripts\python.exe -m pip install matplotlib
```

### 2. Executar os testes

```powershell
.\.venv\Scripts\python.exe testes.py
```

Os testes verificam listas vazias, listas com um elemento, elementos repetidos, listas ordenadas, listas invertidas e outras entradas.

### 3. Executar as medições

```powershell
.\.venv\Scripts\python.exe medir.py
```

O programa realiza 10 repetições para cada tamanho de lista, salva as medições individuais em `dados.csv` e gera os gráficos atualizados.

## Tamanhos utilizados

As listas possuem os seguintes tamanhos:

`5, 10, 20, 30, 50, 75, 100, 200, 500 e 1000`.

## Resultados

O projeto permite comparar o crescimento do tempo de execução e do número de comparações dos algoritmos, além de observar o desempenho da função nativa `sorted()`.

Para visualizar os resultados, abra `grafico_tempos.png`, `grafico_comparacoes.png` e `RELATORIO.md`.
