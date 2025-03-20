import math

def fibonacci(n):
    """Calcula o n-ésimo número de Fibonacci usando a fórmula de Binet."""
    if n < 0:
        raise ValueError("O valor de n deve ser não negativo.")
    
    # Definição do número de ouro (phi) e seu conjugado (psi)
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    
    # Aplica a fórmula de Binet para calcular o n-ésimo termo de Fibonacci
    fib = (phi**n - psi**n) / math.sqrt(5)
    
    # Arredonda o resultado para evitar imprecisões numéricas
    return round(fib)


def fibonot(n):
    """Calcula o K-ésimo número da sequência de Fibonot (número que não pertence à sequência de Fibonacci)."""

    # Inicializa o contador, que conta quantos números de Fibonot já foram encontrados
    contador = 0
    # Definição inicial dos índices de Fibonacci para encontrar a faixa de números Fibonot
    a = 4
    b = 5
    inferior = fibonacci(a)  
    superior = fibonacci(b)  

    # Loop para encontrar a faixa onde o K-ésimo número de Fibonot está localizado
    while contador < n:
        # A quantidade de números Fibonot entre inferior e superior é adicionada ao contador
        contador = superior - inferior + contador - 1

        # Atualiza os índices de Fibonacci para a próxima faixa de números Fibonot
        b += 1
        inferior = superior
        superior = fibonacci(b)

    
    return inferior - abs((abs(contador - n)) + 1)

kesimo = int(input(""))
resultado = fibonot(kesimo)
print(resultado)
