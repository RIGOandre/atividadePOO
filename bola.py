"""
Classe Bola - Lista de Exercícios I
Programação Orientada a Objetos

Cria uma classe que modela uma bola com atributos cor, circunferência e material,
e métodos para trocar e mostrar a cor.
"""

class Bola:
    def __init__(self, cor, circunferencia, material):
        """
        Inicializa uma bola com cor, circunferência e material.
        
        Args:
            cor (str): Cor da bola
            circunferencia (float): Circunferência da bola em cm
            material (str): Material da bola
        """
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocaCor(self, nova_cor):
        """
        Troca a cor da bola.
        
        Args:
            nova_cor (str): Nova cor da bola
        """
        self.cor = nova_cor
        print(f"Cor da bola alterada para: {nova_cor}")
    
    def mostraCor(self):
        """
        Mostra a cor atual da bola.
        
        Returns:
            str: Cor atual da bola
        """
        print(f"A cor da bola é: {self.cor}")
        return self.cor


if __name__ == "__main__":
    # Exemplo de uso da classe Bola
    print("=== TESTE DA CLASSE BOLA ===")
    bola1 = Bola("Vermelha", 30.5, "Borracha")

    print(f"Bola criada - Cor: {bola1.cor}, Circunferência: {bola1.circunferencia}cm, Material: {bola1.material}")
    bola1.mostraCor()
    bola1.trocaCor("Azul")
    bola1.mostraCor()