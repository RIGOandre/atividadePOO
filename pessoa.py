"""
Classe Pessoa - Lista de Exercícios I
Programação Orientada a Objetos

Cria uma classe que modela uma pessoa com atributos nome, idade, peso e altura,
e métodos para envelhecer, engordar, emagrecer e crescer. 
A pessoa cresce 0,5 cm a cada ano enquanto for menor que 21 anos.
"""

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        """
        Inicializa uma pessoa com nome, idade, peso e altura.
        
        Args:
            nome (str): Nome da pessoa
            idade (int): Idade em anos
            peso (float): Peso em kg
            altura (float): Altura em cm
        """
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self, anos=1):
        """
        Envelhece a pessoa. Se for menor que 21 anos, cresce 0,5 cm por ano.
        
        Args:
            anos (int): Quantidade de anos para envelhecer (padrão: 1)
        """
        for _ in range(anos):
            if self.idade < 21:
                self.crescer(0.5)
            self.idade += 1
        print(f"{self.nome} envelheceu {anos} ano(s). Idade atual: {self.idade} anos")
    
    def engordar(self, quilos):
        """
        Aumenta o peso da pessoa.
        
        Args:
            quilos (float): Quantidade de peso a ganhar em kg
        """
        self.peso += quilos
        print(f"{self.nome} ganhou {quilos} kg. Peso atual: {self.peso:.1f} kg")
    
    def emagrecer(self, quilos):
        """
        Diminui o peso da pessoa.
        
        Args:
            quilos (float): Quantidade de peso a perder em kg
        """
        self.peso -= quilos
        if self.peso < 0:
            self.peso = 0
        print(f"{self.nome} perdeu {quilos} kg. Peso atual: {self.peso:.1f} kg")
    
    def crescer(self, centimetros):
        """
        Aumenta a altura da pessoa.
        
        Args:
            centimetros (float): Quantidade a crescer em cm
        """
        self.altura += centimetros
        print(f"{self.nome} cresceu {centimetros} cm. Altura atual: {self.altura:.1f} cm")
    
    def mostrarInfo(self):
        """
        Mostra todas as informações da pessoa.
        """
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso:.1f} kg")
        print(f"Altura: {self.altura:.1f} cm")


if __name__ == "__main__":
    print("=== TESTE DA CLASSE PESSOA ===")

    joao = Pessoa("João", 16, 65.0, 170.0)
    print("Informações iniciais:")
    joao.mostrarInfo()

    print("\n--- João envelhece 3 anos ---")
    joao.envelhecer(3)
    joao.mostrarInfo()

    print("\n--- João ganha peso ---")
    joao.engordar(5.5)

    print("\n--- João perde peso ---")
    joao.emagrecer(2.0)

    print("\n--- João envelhece mais 5 anos (não crescerá mais pois já passou dos 21) ---")
    joao.envelhecer(5)
    joao.mostrarInfo()