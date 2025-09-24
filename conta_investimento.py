"""
Classe Conta de Investimento - Lista de Exercícios I
Programação Orientada a Objetos

Conta semelhante à conta bancária com adição de taxa de juros 
para aplicação de rendimentos.
"""

class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        """
        Inicializa uma conta de investimento.
        
        Args:
            saldo_inicial (float): Saldo inicial da conta
            taxa_juros (float): Taxa de juros em porcentagem
        """
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros
    
    def adicione_juros(self):
        """Adiciona juros ao saldo da conta."""
        juros = self.saldo * (self.taxa_juros / 100)
        self.saldo += juros
        print(f"Juros adicionados: R$ {juros:.2f}. Novo saldo: R$ {self.saldo:.2f}")
    
    def obter_saldo(self):
        """
        Retorna o saldo atual.
        
        Returns:
            float: Saldo atual da conta
        """
        return self.saldo


if __name__ == "__main__":
    
    print("=== TESTE DA CLASSE CONTA DE INVESTIMENTO ===")
    poupanca = ContaInvestimento(1000.00, 10)  # R$ 1000 com 10% de juros

    print(f"Saldo inicial: R$ {poupanca.obter_saldo():.2f}")

    for i in range(5):
        print(f"\nAplicação {i+1}:")
        poupanca.adicione_juros()

    print(f"\nSaldo final após 5 aplicações de juros: R$ {poupanca.obter_saldo():.2f}")