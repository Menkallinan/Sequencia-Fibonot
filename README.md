# Sequência de Fibonot

## Descrição do Problema
A Sequência de Fibonacci é uma das mais conhecidas na Matemática, definida pelos termos:

```
1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

Cada termo é a soma dos dois anteriores, e os dois primeiros termos são 1.

Por outro lado, a Sequência de Fibonot é composta pelos números inteiros positivos que **não** pertencem à Sequência de Fibonacci. Alguns dos primeiros termos de Fibonot são:

```
4, 6, 7, 9, 10, 11, 12, 14, 15, ...
```

O desafio deste problema é encontrar o **K-ésimo** termo da Sequência de Fibonot, dado um valor inteiro K.

## Entrada
A entrada consiste em um único inteiro **K** (1 ≤ K ≤ 10⁵), representando a posição do termo desejado na Sequência de Fibonot.

### Exemplo de Entrada:
```
10
```

## Saída
A saída deve conter um único inteiro representando o **K-ésimo** termo da Sequência de Fibonot.

### Exemplo de Saída:
```
19
```

## Como Executar
1. Certifique-se de ter **Python 3** instalado.
2. Salve o código abaixo em um arquivo chamado `fibonot.py`.
3. Execute o script no terminal ou prompt de comando:
   ```sh
   python fibonot.py
   ```
4. Insira o valor de **K** e pressione **Enter** para obter o resultado.

## Explicação do Código
1. **`fibonacci(n)`**: Implementa a Fórmula de Binet para calcular rapidamente o n-ésimo termo de Fibonacci.
2. **`fibonot(n)`**:
   - Encontra os intervalos entre números de Fibonacci, onde os termos de Fibonot aparecem.
   - Um contador rastreia quantos termos de Fibonot foram encontrados.
   - Quando o contador atinge **K**, calcula o valor correto do K-ésimo termo de Fibonot.
3. **Entrada/Saída**:
   - O usuário insere um número **K**.
   - O programa imprime o **K-ésimo termo da sequência de Fibonot**.

## Complexidade
- A função `fibonacci(n)` tem **O(1)** devido à Fórmula de Binet.
- A função `fibonot(n)` itera pelos intervalos de Fibonacci, sendo **O(log K)**, garantindo um desempenho eficiente mesmo para grandes valores de **K**.

## Conclusão
Esta solução utiliza um método matemático eficiente para calcular rapidamente os valores da Sequência de Fibonot sem precisar armazenar toda a sequência, tornando o algoritmo ideal para grandes entradas como **K ≤ 10⁵**.

