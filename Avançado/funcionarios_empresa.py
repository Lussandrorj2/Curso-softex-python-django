class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        self.percentual_bonus = percentual_bonus = 1.1

    def aplicar_bonus(self):
        aplicando_bonus = self.salario * self.percentual_bonus
        return aplicando_bonus

funcionario = Funcionario("João",500)
salario_bonus = funcionario.aplicar_bonus()
print(f"O funcionário {funcionario.nome} recebeu um total de salário + bônus de R$ {salario_bonus:.2f}")

funcionario2 = Funcionario("José",1500)
salario_bonus2 = funcionario2.aplicar_bonus()
print(f"O funcionário {funcionario2.nome} recebeu um total de salário + bônus de R$ {salario_bonus2:.2f}")