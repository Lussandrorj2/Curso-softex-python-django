print('╣ Validação de E-mail ╠')
print('')
while True:
    email = input('Digite seu email: ')
    if "@" in email:
        print('E-mail válido!')
        break
    else:
        print('E-mail inválido! Tente novamente.')