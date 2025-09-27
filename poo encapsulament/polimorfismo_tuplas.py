class Conta():
    def __init__(self, saldo):
        self.saldo = saldo

    def obter_saldo(self):
        return self.saldo
    
class ContaPoupança(Conta):
    def __init__(self, saldo, taxa_juros):
        super().__init__(saldo)
        self.taxa_juros = taxa_juros

    def obter_saldo(self):
        return (self.saldo, self.taxa_juros)
    
conta_comum = Conta(1000)
print(f"conta comum: {conta_comum.obter_saldo()}")

contapoupança = ContaPoupança(2000, 0.05)
print(f"Conta poupança: {contapoupança.obter_saldo()}")