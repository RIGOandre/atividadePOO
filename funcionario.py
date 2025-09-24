"""
Classe Funcionário - Lista de Exercícios I
Programação Orientada a Objetos

Implementa informações básicas de um funcionário e cálculo de aumentos
percentuais sobre o salário.
"""

class Funcionario:
    def __init__(self, nome, salario):
        """
        Inicializa um funcionário.
        
        Args:
            nome (str): Nome do funcionário
            salario (float): Salário atual do funcionário
        """
        self.nome = nome
        self.salario = salario
    
    def obter_nome(self):
        """
        Retorna o nome do funcionário.
        
        Returns:
            str: Nome do funcionário
        """
        return self.nome
    
    def obter_salario(self):
        """
        Retorna o salário atual.
        
        Returns:
            float: Salário atual do funcionário
        """
        return self.salario
    
    def aumentar_salario(self, percentual_aumento):
        """
        Aumenta o salário por uma porcentagem especificada.
        
        Args:
            percentual_aumento (float): Percentual de aumento (ex: 10 para 10%)
        """
        if percentual_aumento < 0:
            print("Percentual de aumento não pode ser negativo.")
            return
        
        aumento = self.salario * (percentual_aumento / 100)
        self.salario += aumento
        
        print(f"Salário aumentado em {percentual_aumento}%.")
        print(f"Aumento: R$ {aumento:.2f}")
        print(f"Novo salário: R$ {self.salario:.2f}")


if __name__ == "__main__":
    # Exemplo conforme especificação
    print("=== TESTE DA CLASSE FUNCIONÁRIO ===")
    harry = Funcionario("Harry", 25000)
    
    print(f"Funcionário: {harry.obter_nome()}")
    print(f"Salário inicial: R$ {harry.obter_salario():.2f}")
    
    print("\nAumentando salário em 10%:")
    harry.aumentar_salario(10)
    
    print("\nAumentando salário em 27%:")
    harry.aumentar_salario(27)
    
    print("\nTestando aumento negativo:")
    harry.aumentar_salario(-5)