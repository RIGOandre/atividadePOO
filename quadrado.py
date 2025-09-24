"""
Classe Quadrado - Lista de Exercícios I
Programação Orientada a Objetos

Cria uma classe que modela um quadrado com atributo tamanho do lado 
e métodos para mudar valor do lado, retornar valor do lado e calcular área.
"""

class Quadrado:
    def __init__(self, lado):
        """
        Inicializa um quadrado com o tamanho do lado.
        
        Args:
            lado (float): Tamanho do lado do quadrado
        """
        self.lado = lado
    
    def mudarLado(self, novo_lado):
        """
        Muda o valor do lado do quadrado.
        
        Args:
            novo_lado (float): Novo tamanho do lado
        """
        self.lado = novo_lado
        print(f"Lado do quadrado alterado para: {novo_lado}")
    
    def retornarLado(self):
        """
        Retorna o valor atual do lado do quadrado.
        
        Returns:
            float: Tamanho atual do lado
        """
        return self.lado
    
    def calcularArea(self):
        """
        Calcula a área do quadrado.
        
        Returns:
            float: Área do quadrado (lado²)
        """
        area = self.lado ** 2
        return area


if __name__ == "__main__":
    print("=== TESTE DA CLASSE QUADRADO ===")
    quadrado1 = Quadrado(5)

    print(f"Quadrado criado com lado: {quadrado1.retornarLado()}")
    print(f"Área do quadrado: {quadrado1.calcularArea()}")

    quadrado1.mudarLado(8)
    print(f"Novo lado: {quadrado1.retornarLado()}")
    print(f"Nova área: {quadrado1.calcularArea()}")