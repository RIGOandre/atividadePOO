"""
Classe Retângulo - Lista de Exercícios I
Programação Orientada a Objetos

Cria uma classe que modela um retângulo com atributos largura e altura, 
métodos para mudar valores dos lados, retornar valores dos lados, calcular área 
e perímetro. Inclui programa para calcular quantidade de pisos e rodapés necessários.
"""

import math

class Retangulo:
    def __init__(self, largura, altura):
        """
        Inicializa um retângulo com largura e altura.
        
        Args:
            largura (float): Largura do retângulo
            altura (float): Altura do retângulo
        """
        self.largura = largura
        self.altura = altura
    
    def mudarLados(self, nova_largura, nova_altura):
        """
        Muda os valores dos lados do retângulo.
        
        Args:
            nova_largura (float): Nova largura
            nova_altura (float): Nova altura
        """
        self.largura = nova_largura
        self.altura = nova_altura
        print(f"Lados alterados para - Largura: {nova_largura}, Altura: {nova_altura}")
    
    def retornarLados(self):
        """
        Retorna os valores atuais dos lados.
        
        Returns:
            tuple: (largura, altura)
        """
        return (self.largura, self.altura)
    
    def calcularArea(self):
        """
        Calcula a área do retângulo.
        
        Returns:
            float: Área do retângulo (largura × altura)
        """
        return self.largura * self.altura
    
    def calcularPerimetro(self):
        """
        Calcula o perímetro do retângulo.
        
        Returns:
            float: Perímetro do retângulo (2 × (largura + altura))
        """
        return 2 * (self.largura + self.altura)


def calcular_pisos_e_rodapes():
    """
    Programa que calcula a quantidade de pisos e rodapés necessários para um local.
    """
    print("\n=== CALCULADORA DE PISOS E RODAPÉS ===")
    
    # Entrada de dados do usuário
    try:
        largura = float(input("Digite a largura do local (em metros): "))
        altura = float(input("Digite a altura do local (em metros): "))
        
        # Dimensões do piso (exemplo: 60cm x 60cm = 0.6m x 0.6m)
        lado_piso = float(input("Digite o lado do piso quadrado (em metros, ex: 0.6 para 60cm): "))
        
        # Criar objeto retângulo com as medidas do local
        local = Retangulo(largura, altura)
        
        # Calcular área do local
        area_local = local.calcularArea()
        print(f"\nÁrea do local: {area_local:.2f} m²")
        
        # Calcular área de um piso
        area_piso = lado_piso ** 2
        print(f"Área de um piso: {area_piso:.4f} m²")
        
        # Calcular quantidade de pisos necessários (com margem de 10% para perdas)
        pisos_necessarios = math.ceil(area_local / area_piso * 1.1)
        print(f"Quantidade de pisos necessários (com 10% margem): {pisos_necessarios} unidades")
        
        # Calcular perímetro para rodapés
        perimetro_local = local.calcularPerimetro()
        print(f"Perímetro do local: {perimetro_local:.2f} m")
        
        # Considerar largura da porta (geralmente 0.8m)
        largura_porta = float(input("Digite a largura da porta (em metros, ex: 0.8): "))
        rodape_necessario = perimetro_local - largura_porta
        print(f"Rodapé necessário (descontando porta): {rodape_necessario:.2f} m")
        
        return local, pisos_necessarios, rodape_necessario
        
    except ValueError:
        print("Erro: Digite apenas números válidos!")
        return None, 0, 0


if __name__ == "__main__":
    # Teste da classe Retângulo
    print("=== TESTE DA CLASSE RETÂNGULO ===")
    retangulo1 = Retangulo(10, 6)

    largura, altura = retangulo1.retornarLados()
    print(f"Retângulo criado - Largura: {largura}, Altura: {altura}")
    print(f"Área: {retangulo1.calcularArea()} m²")
    print(f"Perímetro: {retangulo1.calcularPerimetro()} m")

    retangulo1.mudarLados(12, 8)
    print(f"Nova área: {retangulo1.calcularArea()} m²")
    print(f"Novo perímetro: {retangulo1.calcularPerimetro()} m")
    
    # Exemplo prático da calculadora de pisos e rodapés
    print("\n=== EXEMPLO PRÁTICO: CALCULADORA DE PISOS E RODAPÉS ===")

    # Simulando um quarto de 4m x 3m
    local_exemplo = Retangulo(4.0, 3.0)
    area_local = local_exemplo.calcularArea()
    perimetro_local = local_exemplo.calcularPerimetro()

    print(f"Local exemplo: Quarto de 4m x 3m")
    print(f"Área do local: {area_local} m²")
    print(f"Perímetro do local: {perimetro_local} m")

    # Piso de 60cm x 60cm
    lado_piso = 0.6
    area_piso = lado_piso ** 2
    pisos_necessarios = math.ceil(area_local / area_piso * 1.1)  # 10% margem

    print(f"\nPiso escolhido: {lado_piso}m x {lado_piso}m")
    print(f"Área de um piso: {area_piso} m²")
    print(f"Quantidade de pisos necessários (com 10% margem): {pisos_necessarios} unidades")

    # Rodapé (descontando porta de 0.8m)
    largura_porta = 0.8
    rodape_necessario = perimetro_local - largura_porta
    print(f"\nRodapé necessário (descontando porta de {largura_porta}m): {rodape_necessario} m")
    
    # Para usar a calculadora interativa, descomente a linha abaixo:
    # calcular_pisos_e_rodapes()