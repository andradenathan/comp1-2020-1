from math import pi, fabs

def serie(n):
    """
    Dada uma fórmula calcula a soma dessa série até o termo n.
    :param n: int -> int
    :return: float -> float
    """
    somatoria = 0
    for k in range(0, n + 1):
        somatoria = (-1) ** k / (2 * k + 1)

    return somatoria

def erro_serie(n = 0.01):
    """
    Calcula a soma da série com erro inferior a 0,01 e retorna quantos termos foram somados enquanto o erro era
    menor do que 0,01.
    :param n: int -> int
    :param termos: int -> int
    :return: tuple -> tuple
    """
    contador = 0
    soma = serie(n)
    while fabs(pi / 4 - soma) > n:
        contador += 1
        soma = serie(contador)

    return soma, contador

def buscar(lista, nome):
    """
    Busca um usuário a partir do seu nome registrado e adiciona em uma nova lista de contatos.
    :param lista: list -> list
    :param nome: str -> str
    :return: list -> list
    """
    contatos = []
    for l in range(0, len(lista)):
        if nome.lower() in lista[l][0].lower():
            contatos.append(lista[l])

    return contatos