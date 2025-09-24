"""
Classe Bichinho Virtual (Tamagushi) - Lista de Exercícios I
Programação Orientada a Objetos

Modela um Tamagushi com atributos nome, fome, saúde e idade. 
O humor é calculado automaticamente baseado na fome e saúde.
"""

class BichinhoVirtual:
    def __init__(self, nome, fome=50, saude=50, idade=0):
        """
        Inicializa um bichinho virtual (Tamagushi).
        
        Args:
            nome (str): Nome do bichinho
            fome (int): Nível de fome (0-100, padrão: 50)
            saude (int): Nível de saúde (0-100, padrão: 50)
            idade (int): Idade do bichinho (padrão: 0)
        """
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
    
    def alterar_nome(self, novo_nome):
        """
        Altera o nome do bichinho.
        
        Args:
            novo_nome (str): Novo nome do bichinho
        """
        self.nome = novo_nome
    
    def alterar_fome(self, valor):
        """
        Altera o nível de fome (mantém entre 0-100).
        
        Args:
            valor (int): Novo nível de fome
        """
        self.fome = max(0, min(100, valor))
    
    def alterar_saude(self, valor):
        """
        Altera o nível de saúde (mantém entre 0-100).
        
        Args:
            valor (int): Novo nível de saúde
        """
        self.saude = max(0, min(100, valor))
    
    def alterar_idade(self, valor):
        """
        Altera a idade do bichinho.
        
        Args:
            valor (int): Nova idade
        """
        self.idade = max(0, valor)
    
    def retornar_nome(self):
        """Retorna o nome do bichinho."""
        return self.nome
    
    def retornar_fome(self):
        """Retorna o nível de fome."""
        return self.fome
    
    def retornar_saude(self):
        """Retorna o nível de saúde."""
        return self.saude
    
    def retornar_idade(self):
        """Retorna a idade do bichinho."""
        return self.idade
    
    def retornar_humor(self):
        """
        Calcula e retorna o humor baseado na fome e saúde.
        
        Returns:
            str: Descrição do humor atual
        """
        humor = (self.saude + (100 - self.fome)) / 2
        if humor >= 80:
            return "Muito Feliz"
        elif humor >= 60:
            return "Feliz"
        elif humor >= 40:
            return "Normal"
        elif humor >= 20:
            return "Triste"
        else:
            return "Muito Triste"


if __name__ == "__main__":
    # Exemplo de uso da classe BichinhoVirtual
    print("=== TESTE DA CLASSE BICHINHO VIRTUAL ===")
    bichinho = BichinhoVirtual("Tamagotchi")

    print(f"Nome: {bichinho.retornar_nome()}")
    print(f"Fome: {bichinho.retornar_fome()}")
    print(f"Saúde: {bichinho.retornar_saude()}")
    print(f"Idade: {bichinho.retornar_idade()}")
    print(f"Humor: {bichinho.retornar_humor()}")

    print("\n--- Alterando valores ---")
    bichinho.alterar_fome(20)  # Diminui fome (alimenta)
    bichinho.alterar_saude(80)  # Melhora saúde
    bichinho.alterar_idade(5)   # Envelhece

    print(f"Nova fome: {bichinho.retornar_fome()}")
    print(f"Nova saúde: {bichinho.retornar_saude()}")
    print(f"Nova idade: {bichinho.retornar_idade()}")
    print(f"Novo humor: {bichinho.retornar_humor()}")