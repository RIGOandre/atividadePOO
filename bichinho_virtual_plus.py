"""
Classes Bichinho Virtual Plus e Fazenda de Bichinhos - Lista de Exercícios I
Programação Orientada a Objetos

Evolução do bichinho virtual com recursos aprimorados e sistema de fazenda
para gerenciar múltiplos bichinhos.
"""

class BichinhoVirtualPlus:
    def __init__(self, nome, fome=0, tedio=0):
        """
        Inicializa um bichinho virtual aprimorado.
        
        Args:
            nome (str): Nome do bichinho
            fome (int): Nível inicial de fome (0-100)
            tedio (int): Nível inicial de tédio (0-100)
        """
        self.nome = nome
        self.fome = max(0, min(fome, 100))  # Garantir que esteja entre 0-100
        self.tedio = max(0, min(tedio, 100))
    
    def alterar_nome(self, novo_nome):
        """
        Altera o nome do bichinho.
        
        Args:
            novo_nome (str): Novo nome para o bichinho
        """
        nome_anterior = self.nome
        self.nome = novo_nome
        print(f"Nome alterado de '{nome_anterior}' para '{self.nome}'")
    
    def alterar_fome(self, nova_fome):
        """
        Altera o nível de fome.
        
        Args:
            nova_fome (int): Novo nível de fome (0-100)
        """
        fome_anterior = self.fome
        self.fome = max(0, min(nova_fome, 100))
        print(f"Fome alterada de {fome_anterior} para {self.fome}")
    
    def alterar_tedio(self, novo_tedio):
        """
        Altera o nível de tédio.
        
        Args:
            novo_tedio (int): Novo nível de tédio (0-100)
        """
        tedio_anterior = self.tedio
        self.tedio = max(0, min(novo_tedio, 100))
        print(f"Tédio alterado de {tedio_anterior} para {self.tedio}")
    
    def retornar_nome(self):
        """
        Retorna o nome do bichinho.
        
        Returns:
            str: Nome do bichinho
        """
        return self.nome
    
    def retornar_fome(self):
        """
        Retorna o nível de fome.
        
        Returns:
            int: Nível de fome (0-100)
        """
        return self.fome
    
    def retornar_tedio(self):
        """
        Retorna o nível de tédio.
        
        Returns:
            int: Nível de tédio (0-100)
        """
        return self.tedio
    
    def retornar_humor(self):
        """
        Calcula e retorna o humor do bichinho.
        
        Returns:
            int: Humor calculado (200 - fome - tédio)
        """
        return 200 - self.fome - self.tedio
    
    def comer(self, quantidade=10):
        """
        Alimenta o bichinho, reduzindo a fome.
        
        Args:
            quantidade (int): Quantidade que reduzirá a fome (padrão: 10)
        """
        fome_anterior = self.fome
        self.fome = max(0, self.fome - quantidade)
        print(f"{self.nome} comeu! Fome: {fome_anterior} → {self.fome}")
    
    def brincar(self, quantidade=15):
        """
        Brinca com o bichinho, reduzindo o tédio.
        
        Args:
            quantidade (int): Quantidade que reduzirá o tédio (padrão: 15)
        """
        tedio_anterior = self.tedio
        self.tedio = max(0, self.tedio - quantidade)
        print(f"{self.nome} brincou! Tédio: {tedio_anterior} → {self.tedio}")
    
    def obter_status(self):
        """
        Retorna o status completo do bichinho.
        
        Returns:
            str: Status formatado com todos os dados
        """
        humor = self.retornar_humor()
        
        if humor > 150:
            estado_humor = "Muito Feliz! 😄"
        elif humor > 100:
            estado_humor = "Feliz 😊"
        elif humor > 50:
            estado_humor = "Normal 😐"
        elif humor > 20:
            estado_humor = "Triste 😢"
        else:
            estado_humor = "Muito Triste 😭"
        
        return (f"Nome: {self.nome}\n"
                f"Fome: {self.fome}/100\n"
                f"Tédio: {self.tedio}/100\n"
                f"Humor: {humor}/200 - {estado_humor}")


class FazendaBichinhos:
    def __init__(self):
        """Inicializa uma fazenda vazia de bichinhos."""
        self.bichinhos = []
    
    def adicionar_bichinho(self, bichinho):
        """
        Adiciona um bichinho à fazenda.
        
        Args:
            bichinho (BichinhoVirtualPlus): Bichinho a ser adicionado
        """
        if isinstance(bichinho, BichinhoVirtualPlus):
            self.bichinhos.append(bichinho)
            print(f"Bichinho '{bichinho.retornar_nome()}' adicionado à fazenda!")
        else:
            print("Erro: Objeto não é um BichinhoVirtualPlus válido.")
    
    def ouvir_todos(self):
        """
        Mostra o status de todos os bichinhos da fazenda.
        """
        if not self.bichinhos:
            print("Fazenda vazia! Não há bichinhos.")
            return
        
        print("=== STATUS DE TODOS OS BICHINHOS ===")
        for i, bichinho in enumerate(self.bichinhos, 1):
            print(f"\n--- Bichinho {i} ---")
            print(bichinho.obter_status())
    
    def brincar_com_todos(self):
        """Brinca com todos os bichinhos da fazenda."""
        if not self.bichinhos:
            print("Fazenda vazia! Não há bichinhos para brincar.")
            return
        
        print("=== BRINCANDO COM TODOS ===")
        for bichinho in self.bichinhos:
            bichinho.brincar()
    
    def alimentar_todos(self):
        """Alimenta todos os bichinhos da fazenda."""
        if not self.bichinhos:
            print("Fazenda vazia! Não há bichinhos para alimentar.")
            return
        
        print("=== ALIMENTANDO TODOS ===")
        for bichinho in self.bichinhos:
            bichinho.comer()
    
    def obter_mais_feliz(self):
        """
        Encontra o bichinho mais feliz da fazenda.
        
        Returns:
            BichinhoVirtualPlus: Bichinho com maior humor, ou None se fazenda vazia
        """
        if not self.bichinhos:
            return None
        
        mais_feliz = max(self.bichinhos, key=lambda b: b.retornar_humor())
        return mais_feliz
    
    def obter_mais_faminto(self):
        """
        Encontra o bichinho mais faminto da fazenda.
        
        Returns:
            BichinhoVirtualPlus: Bichinho com maior fome, ou None se fazenda vazia
        """
        if not self.bichinhos:
            return None
        
        mais_faminto = max(self.bichinhos, key=lambda b: b.retornar_fome())
        return mais_faminto
    
    def obter_quantidade(self):
        """
        Retorna a quantidade de bichinhos na fazenda.
        
        Returns:
            int: Número de bichinhos
        """
        return len(self.bichinhos)
    
    def porta_secreta(self):
        """
        Funcionalidade especial oculta da fazenda.
        Easter egg para usuários que descobrirem este método.
        """
        print("🎉 PORTA SECRETA ENCONTRADA! 🎉")
        print("Você descobriu a porta secreta da fazenda!")
        print("Como recompensa, todos os bichinhos ficaram super felizes!")
        
        for bichinho in self.bichinhos:
            bichinho.alterar_fome(0)
            bichinho.alterar_tedio(0)
        
        print("Todos os bichinhos estão agora com fome e tédio zerados!")


if __name__ == "__main__":
    print("=== TESTE BICHINHO VIRTUAL PLUS ===")
    
    # Criando bichinhos
    bichinho1 = BichinhoVirtualPlus("Tamagushi", 50, 60)
    bichinho2 = BichinhoVirtualPlus("Pikachu", 30, 40)
    bichinho3 = BichinhoVirtualPlus("Chocobo", 80, 20)
    
    print("Status inicial dos bichinhos:")
    for i, b in enumerate([bichinho1, bichinho2, bichinho3], 1):
        print(f"\n--- Bichinho {i} ---")
        print(b.obter_status())
    
    print("\n=== TESTE FAZENDA DE BICHINHOS ===")
    
    # Criando fazenda e adicionando bichinhos
    fazenda = FazendaBichinhos()
    fazenda.adicionar_bichinho(bichinho1)
    fazenda.adicionar_bichinho(bichinho2)
    fazenda.adicionar_bichinho(bichinho3)
    
    print(f"\nFazenda tem {fazenda.obter_quantidade()} bichinhos")
    
    # Testando funcionalidades da fazenda
    fazenda.ouvir_todos()
    
    print("\n=== BRINCANDO E ALIMENTANDO ===")
    fazenda.brincar_com_todos()
    fazenda.alimentar_todos()
    
    print("\n=== STATUS APÓS CUIDADOS ===")
    fazenda.ouvir_todos()
    
    # Encontrando extremos
    mais_feliz = fazenda.obter_mais_feliz()
    mais_faminto = fazenda.obter_mais_faminto()
    
    print(f"\nMais feliz: {mais_feliz.retornar_nome()} (humor: {mais_feliz.retornar_humor()})")
    print(f"Mais faminto: {mais_faminto.retornar_nome()} (fome: {mais_faminto.retornar_fome()})")
    
    # Teste da porta secreta
    print("\n=== DESCOBRINDO A PORTA SECRETA ===")
    fazenda.porta_secreta()
    
    print("\n=== STATUS FINAL ===")
    fazenda.ouvir_todos()