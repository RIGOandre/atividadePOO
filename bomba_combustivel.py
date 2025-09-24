"""
Classe Bomba de Combustível - Lista de Exercícios I
Programação Orientada a Objetos

Implementa uma bomba de combustível com tipo, valor por litro e quantidade disponível. 
Métodos para abastecimento por valor/litro e alteração de configurações.
"""

class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        """
        Inicializa uma bomba de combustível.
        
        Args:
            tipo_combustivel (str): Tipo do combustível (ex: Gasolina, Álcool, Diesel)
            valor_litro (float): Preço por litro
            quantidade_combustivel (float): Quantidade disponível na bomba
        """
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
    
    def abastecer_por_valor(self, valor):
        """
        Abastece informando o valor a ser gasto.
        
        Args:
            valor (float): Valor em reais para abastecimento
            
        Returns:
            float: Quantidade de litros abastecida
        """
        litros = valor / self.valor_litro
        if litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros
            print(f"Abastecido {litros:.2f} litros por R$ {valor:.2f}")
            return litros
        else:
            print("Quantidade insuficiente de combustível na bomba!")
            return 0
    
    def abastecer_por_litro(self, litros):
        """
        Abastece informando a quantidade de litros.
        
        Args:
            litros (float): Quantidade de litros para abastecimento
            
        Returns:
            float: Valor a ser pago
        """
        if litros <= self.quantidade_combustivel:
            valor = litros * self.valor_litro
            self.quantidade_combustivel -= litros
            print(f"Valor a pagar: R$ {valor:.2f} por {litros} litros")
            return valor
        else:
            print("Quantidade insuficiente de combustível na bomba!")
            return 0
    
    def alterar_valor(self, novo_valor):
        """Altera o valor do litro do combustível."""
        self.valor_litro = novo_valor
        print(f"Valor do litro alterado para R$ {novo_valor:.2f}")
    
    def alterar_combustivel(self, novo_tipo):
        """Altera o tipo do combustível."""
        self.tipo_combustivel = novo_tipo
        print(f"Tipo de combustível alterado para {novo_tipo}")
    
    def alterar_quantidade_combustivel(self, nova_quantidade):
        """Altera a quantidade de combustível restante na bomba."""
        self.quantidade_combustivel = nova_quantidade
        print(f"Quantidade de combustível alterada para {nova_quantidade} litros")
    
    def status(self):
        """Mostra o status atual da bomba."""
        print(f"Tipo: {self.tipo_combustivel}")
        print(f"Valor/Litro: R$ {self.valor_litro:.2f}")
        print(f"Quantidade disponível: {self.quantidade_combustivel:.2f} litros")


if __name__ == "__main__":
    # Exemplo de uso da classe BombaCombustivel
    print("=== TESTE DA CLASSE BOMBA DE COMBUSTÍVEL ===")
    bomba = BombaCombustivel("Gasolina", 5.50, 1000)

    print("--- Status inicial da bomba ---")
    bomba.status()

    print("\n--- Abastecimento por valor ---")
    bomba.abastecer_por_valor(100)

    print("\n--- Abastecimento por litro ---")
    bomba.abastecer_por_litro(20)

    print("\n--- Alterando configurações ---")
    bomba.alterar_valor(5.75)
    bomba.alterar_combustivel("Etanol")

    print("\n--- Status final da bomba ---")
    bomba.status()