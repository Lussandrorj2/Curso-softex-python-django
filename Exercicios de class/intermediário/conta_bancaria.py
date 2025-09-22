class Conta_Bancaria():
    def __init__(self, titular, saldoinicial):
        self.titular = titular
        self.saldo = saldoinicial
        self.saldoinicial = saldoinicial

    def depositar(self):
        valor = float(input("Digite um valor para realizar o depósito: "))
        if valor > 0:
            self.saldo += valor
            print(f"Depósito do valor {valor:.2f} realizado com sucesso.".replace(".",","))
            print(f"Novo saldo: {self.saldo:.2f}".replace(".",","))
        else:
            print("Valor inválido. Tente novamente")
        return self.saldo  
    
    def sacar(self):
        valor = float(input("Digite um valor para realizar o saque: "))
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque do valor {valor:.2f} realizado com sucesso.".replace(".",","))
            print(f"Novo saldo após saque: {self.saldo:.2f}".replace(".",","))
        else:
            print("Saldo insuficiente.")
        return self.saldo
    
usuario = Conta_Bancaria("João",200.00)
print(f"Olá, {usuario.titular}!") 
print(f'Seu saldo atual é R$ {usuario.saldoinicial:.2f}'.replace(".",","))


usuario.depositar()
usuario.sacar()
    
#novo_saldo = usuario.depositar(300)
#saque = usuario.sacar(100)

#print(f"Titular: {usuario.titular} e Saldo: {usuario.saloinicial:.2f}")
#print(f"Novo saldo: {novo_saldo:.2f}")
#print(f"Novo saldo após o saque {saque:.2f}")