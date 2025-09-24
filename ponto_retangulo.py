"""
Classes Ponto e Retângulo - Lista de Exercícios I
Programação Orientada a Objetos

Implementa classe Ponto com coordenadas x,y e classe Retângulo com vértice 
de partida (Ponto), largura e altura. Inclui funções para imprimir pontos 
e encontrar centro do retângulo.
"""

class Ponto:
    def __init__(self, x, y):
        """
        Inicializa um ponto com coordenadas x e y.
        
        Args:
            x (float): Coordenada x
            y (float): Coordenada y
        """
        self.x = x
        self.y = y

class RetanguloGeometrico:
    def __init__(self, ponto_inicial, largura, altura):
        """
        Inicializa um retângulo com ponto inicial, largura e altura.
        
        Args:
            ponto_inicial (Ponto): Vértice inferior esquerdo do retângulo
            largura (float): Largura do retângulo
            altura (float): Altura do retângulo
        """
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

def imprimir_ponto(ponto):
    """
    Imprime os valores de um ponto.
    
    Args:
        ponto (Ponto): Ponto a ser impresso
    """
    print(f"Ponto: ({ponto.x}, {ponto.y})")

def encontrar_centro(retangulo):
    """
    Encontra o centro de um retângulo.
    
    Args:
        retangulo (RetanguloGeometrico): Retângulo para calcular o centro
        
    Returns:
        Ponto: Ponto que representa o centro do retângulo
    """
    centro_x = retangulo.ponto_inicial.x + retangulo.largura / 2
    centro_y = retangulo.ponto_inicial.y + retangulo.altura / 2
    return Ponto(centro_x, centro_y)


if __name__ == "__main__":
    # Exemplo de uso das classes Ponto e Retângulo
    print("=== TESTE DAS CLASSES PONTO E RETÂNGULO ===")

    # Criando pontos
    ponto1 = Ponto(0, 0)
    ponto2 = Ponto(5, 3)

    print("--- Pontos criados ---")
    print("Ponto 1:", end=" ")
    imprimir_ponto(ponto1)
    print("Ponto 2:", end=" ")
    imprimir_ponto(ponto2)

    # Criando retângulos
    ret1 = RetanguloGeometrico(ponto1, 10, 5)
    ret2 = RetanguloGeometrico(ponto2, 8, 6)

    print("\n--- Retângulos criados ---")
    print(f"Retângulo 1: Início{ponto1.x, ponto1.y}, Largura: {ret1.largura}, Altura: {ret1.altura}")
    print(f"Retângulo 2: Início{ponto2.x, ponto2.y}, Largura: {ret2.largura}, Altura: {ret2.altura}")

    # Encontrando centros
    centro1 = encontrar_centro(ret1)
    centro2 = encontrar_centro(ret2)

    print("\n--- Centros dos retângulos ---")
    print("Centro do retângulo 1:", end=" ")
    imprimir_ponto(centro1)
    print("Centro do retângulo 2:", end=" ")
    imprimir_ponto(centro2)

    print("\n--- Exemplo de alteração ---")
    # Alterando retângulo 1
    ret1.ponto_inicial = Ponto(2, 1)
    ret1.largura = 12
    ret1.altura = 8

    novo_centro = encontrar_centro(ret1)
    print("Novo centro do retângulo 1:", end=" ")
    imprimir_ponto(novo_centro)