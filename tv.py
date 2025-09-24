"""
Classe TV - Lista de Exercícios I
Programação Orientada a Objetos

Simula um televisor com controle de canal e volume, 
garantindo que permaneçam dentro de faixas válidas.
"""

class TV:
    def __init__(self):
        """
        Inicializa uma TV com configurações padrão.
        Canal inicial: 1, Volume inicial: 10
        Faixas válidas: Canal 1-100, Volume 0-50
        """
        self.canal = 1
        self.volume = 10
        self.canal_min = 1
        self.canal_max = 100
        self.volume_min = 0
        self.volume_max = 50
    
    def mudar_canal(self, novo_canal):
        """
        Muda o canal da TV dentro da faixa válida.
        
        Args:
            novo_canal (int): Número do canal desejado
        """
        if self.canal_min <= novo_canal <= self.canal_max:
            self.canal = novo_canal
            print(f"Canal alterado para: {self.canal}")
        else:
            print(f"Canal inválido! Use valores entre {self.canal_min} e {self.canal_max}")
    
    def aumentar_volume(self):
        """Aumenta o volume em 1 unidade se não estiver no máximo."""
        if self.volume < self.volume_max:
            self.volume += 1
            print(f"Volume: {self.volume}")
        else:
            print("Volume já está no máximo!")
    
    def diminuir_volume(self):
        """Diminui o volume em 1 unidade se não estiver no mínimo."""
        if self.volume > self.volume_min:
            self.volume -= 1
            print(f"Volume: {self.volume}")
        else:
            print("Volume já está no mínimo!")
    
    def status(self):
        """
        Retorna o status atual da TV.
        
        Returns:
            str: Status com canal e volume atuais
        """
        return f"Canal: {self.canal} | Volume: {self.volume}"


if __name__ == "__main__":
    # Exemplo de uso da classe TV
    print("=== TESTE DA CLASSE TV ===")
    tv = TV()

    print(f"Status inicial: {tv.status()}")
    tv.mudar_canal(25)
    tv.aumentar_volume()
    tv.aumentar_volume()
    tv.diminuir_volume()
    print(f"Status final: {tv.status()}")

    # Testando limites
    tv.mudar_canal(150)  # Canal inválido
    tv.volume = 50  # Setando volume máximo
    tv.aumentar_volume()  # Tentando aumentar além do máximo