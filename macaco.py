"""
Classe Macaco - Lista de Exercícios I
Programação Orientada a Objetos

Desenvolve uma classe Macaco com nome e bucho (estômago), incluindo métodos 
para comer, ver bucho e digerir. Permite teste de canibalismo entre macacos.
"""

class Macaco:
    def __init__(self, nome):
        """
        Inicializa um macaco com nome e bucho vazio.
        
        Args:
            nome (str): Nome do macaco
        """
        self.nome = nome
        self.bucho = []
    
    def comer(self, alimento):
        """
        Faz o macaco comer um alimento.
        
        Args:
            alimento (str): Nome do alimento a ser consumido
        """
        self.bucho.append(alimento)
        print(f"{self.nome} comeu {alimento}")
    
    def ver_bucho(self):
        """Mostra o conteúdo do estômago do macaco."""
        if self.bucho:
            print(f"Bucho de {self.nome} contém: {', '.join(self.bucho)}")
        else:
            print(f"Bucho de {self.nome} está vazio")
    
    def digerir(self):
        """Remove o primeiro alimento do estômago (digestão)."""
        if self.bucho:
            alimento_digerido = self.bucho.pop(0)
            print(f"{self.nome} digeriu {alimento_digerido}")
        else:
            print(f"{self.nome} não tem nada para digerir")


if __name__ == "__main__":
    # Exemplo de uso da classe Macaco
    print("=== TESTE DA CLASSE MACACO ===")

    # Criando dois macacos
    macaco1 = Macaco("Kong")
    macaco2 = Macaco("Bananas")

    print("--- Alimentando os macacos ---")

    # Alimentando macaco1 com diferentes alimentos
    macaco1.comer("banana")
    macaco1.ver_bucho()

    macaco1.comer("maçã")
    macaco1.ver_bucho()

    macaco1.comer("manga")
    macaco1.ver_bucho()

    print("\n--- Alimentando macaco2 ---")
    # Alimentando macaco2
    macaco2.comer("coco")
    macaco2.ver_bucho()

    macaco2.comer("abacaxi")
    macaco2.ver_bucho()

    print("\n--- Teste de Canibalismo ---")
    # Teste interessante: macaco comendo outro macaco (nome)
    macaco1.comer(macaco2.nome)  # Kong "come" Bananas
    macaco1.ver_bucho()

    print("\n--- Processo de Digestão ---")
    macaco1.digerir()  # Digere primeiro item (banana)
    macaco1.ver_bucho()

    macaco1.digerir()  # Digere segundo item (maçã)
    macaco1.ver_bucho()

    # Tentando digerir quando o bucho está vazio
    macaco2.digerir()
    macaco2.digerir()
    macaco2.ver_bucho()