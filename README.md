# Sequência de Fibonot

## Visão Geral
A **Sequência de Fibonot** é formada pelos números inteiros positivos que **não pertencem** à Sequência de Fibonacci.
O problema consiste em encontrar o **K-ésimo** termo da Sequência de Fibonot, dado um valor inteiro **K**.

Este problema está disponível no site **beecrowd**, sob o número **2846**.

## Definição do Problema
A **Sequência de Fibonacci** é definida pelos termos:
```
1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```
Cada termo é a soma dos dois anteriores, e os dois primeiros termos são **1**.

Por outro lado, a **Sequência de Fibonot** é composta pelos números que **não** pertencem à Sequência de Fibonacci. Alguns dos primeiros termos de Fibonot são:
```
4, 6, 7, 9, 10, 11, 12, 14, 15, ...
```

## Entrada
A entrada consiste em um único inteiro **K** (**1 ≤ K ≤ 10⁵**), representando a posição do termo desejado na Sequência de Fibonot.

### Exemplo de Entrada:
```
9
```

## Saída
A saída consiste em um único inteiro representando o **K-ésimo** termo da Sequência de Fibonot.

### Exemplo de Saída:
```
15
```

## Como Executar
1. Certifique-se de ter **Python 3** instalado.
2. Salve o código em um arquivo chamado `fibonot.py`.
3. Execute o script no terminal ou prompt de comando:
   ```sh
   python fibonot.py
   ```
4. Insira o valor de **K** e pressione **Enter** para obter o resultado.

## Explicação da Solução

### Algoritmo
1. **`fibonacci(n)`**: Utiliza a **Fórmula de Binet** para calcular rapidamente o n-ésimo termo de Fibonacci.
2. **`fibonot(k)`**:
   - Identifica os intervalos entre os números de Fibonacci, onde os termos de Fibonot estão localizados.
   - Um contador rastreia quantos termos de Fibonot foram encontrados.
   - Quando o contador atinge **K**, determina o K-ésimo termo corretamente.

### Complexidade
- A função `fibonacci(n)` tem complexidade **O(1)** devido à Fórmula de Binet.
- A função `fibonot(k)` itera pelos intervalos entre números de Fibonacci, sendo **O(log K)**, garantindo eficiência mesmo para **K = 100.000**.

## Conclusão
Esta solução aproveita um método matemático eficiente para calcular rapidamente os valores da **Sequência de Fibonot**, sem a necessidade de armazenar toda a sequência. Isso a torna ideal para grandes valores de **K**.

---
**Problema:** [beecrowd 2846 - Sequência de Fibonot](https://www.beecrowd.com.br/judge/pt/problems/view/2846)

