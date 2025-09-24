"""
Classe Conta Corrente - Lista de Exercícios I
Programação Orientada a Objetos

Implementa uma conta corrente com número da conta, nome do correntista e saldo.
Métodos para alterar nome, fazer depósito e saque. 
Saldo é opcional no construtor com valor padrão zero.
"""

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0.0):
        """
        Inicializa uma conta corrente.
        
        Args:
            numero_conta (str): Número da conta
            nome_correntista (str): Nome do correntista
            saldo (float): Saldo inicial (padrão: 0.0)
        """
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
    
    def alterarNome(self, novo_nome):
        """
        Altera o nome do correntista.
        
        Args:
            novo_nome (str): Novo nome do correntista
        """
        nome_anterior = self.nome_correntista
        self.nome_correntista = novo_nome
        print(f"Nome alterado de '{nome_anterior}' para '{novo_nome}'")
    
    def deposito(self, valor):
        """
        Realiza um depósito na conta.
        
        Args:
            valor (float): Valor a ser depositado
        """
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            print(f"Saldo atual: R$ {self.saldo:.2f}")
        else:
            print("Erro: Valor de depósito deve ser positivo!")
    
    def saque(self, valor):
        """
        Realiza um saque da conta.
        
        Args:
            valor (float): Valor a ser sacado
        """
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                print(f"Saldo atual: R$ {self.saldo:.2f}")
            else:
                print(f"Erro: Saldo insuficiente! Saldo atual: R$ {self.saldo:.2f}")
        else:
            print("Erro: Valor de saque deve ser positivo!")
    
    def mostrarConta(self):
        """
        Mostra as informações da conta.
        """
        print(f"Número da conta: {self.numero_conta}")
        print(f"Correntista: {self.nome_correntista}")
        print(f"Saldo: R$ {self.saldo:.2f}")


if __name__ == "__main__":
    # Exemplo de uso da classe ContaCorrente
    print("=== TESTE DA CLASSE CONTA CORRENTE ===")

    # Criando conta com saldo inicial padrão (zero)
    conta1 = ContaCorrente("12345-6", "Maria Silva")
    print("Conta criada:")
    conta1.mostrarConta()

    print("\n--- Fazendo depósito ---")
    conta1.deposito(1000.0)

    print("\n--- Fazendo saque ---")
    conta1.saque(300.0)

    print("\n--- Tentando saque maior que o saldo ---")
    conta1.saque(800.0)

    print("\n--- Alterando nome do correntista ---")
    conta1.alterarNome("Maria Silva Santos")

    print("\n--- Informações finais da conta ---")
    conta1.mostrarConta()

    print("\n--- Criando conta com saldo inicial ---")
    conta2 = ContaCorrente("98765-4", "João Santos", 500.0)
    conta2.mostrarConta()