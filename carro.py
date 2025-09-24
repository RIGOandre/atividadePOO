"""
Classe Carro - Lista de Exercícios I
Programação Orientada a Objetos

Implementa um carro com consumo de combustível (km/litro). 
Métodos para andar, obter gasolina e adicionar gasolina ao tanque.
"""

class Carro:
    def __init__(self, consumo):
        """
        Inicializa um carro com consumo específico.
        
        Args:
            consumo (float): Consumo em km por litro
        """
        self.consumo = consumo  # km por litro
        self.combustivel = 0
    
    def andar(self, distancia):
        """
        Simula o ato de dirigir por uma distância, consumindo combustível.
        
        Args:
            distancia (float): Distância a percorrer em km
        """
        combustivel_necessario = distancia / self.consumo
        if combustivel_necessario <= self.combustivel:
            self.combustivel -= combustivel_necessario
            print(f"Andou {distancia} km. Combustível restante: {self.combustivel:.2f} litros")
        else:
            distancia_possivel = self.combustivel * self.consumo
            self.combustivel = 0
            print(f"Combustível insuficiente! Andou apenas {distancia_possivel:.2f} km")
    
    def obter_gasolina(self):
        """
        Retorna o nível atual de combustível.
        
        Returns:
            float: Quantidade de combustível no tanque
        """
        return self.combustivel
    
    def adicionar_gasolina(self, litros):
        """
        Adiciona combustível ao tanque.
        
        Args:
            litros (float): Quantidade de litros a adicionar
        """
        self.combustivel += litros
        print(f"Adicionado {litros} litros. Total: {self.combustivel} litros")


if __name__ == "__main__":
    print("=== TESTE DA CLASSE CARRO ===")

    meuFusca = Carro(15)  # 15 quilômetros por litro de combustível
    meuFusca.adicionar_gasolina(20)  # abastece com 20 litros de combustível
    meuFusca.andar(100)  # anda 100 quilômetros
    print(f"Combustível restante: {meuFusca.obter_gasolina():.2f} litros")  # Imprime o combustível que resta

    print("\n--- Teste adicional ---")
    print(f"Consumo do carro: {meuFusca.consumo} km/l")
    meuFusca.andar(50)  # Anda mais 50 km
    meuFusca.andar(200)  # Tenta andar mais que o combustível permite