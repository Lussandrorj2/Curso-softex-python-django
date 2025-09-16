print(">>> Conversor de temperatura <<<")

def temperatura():
    celsius = float(input("Digite a temperatura em Celsius: "))
    f = (celsius * 9/5) + 32
    print(f"A temperatura em Celsius é {celsius}º e convertida para fahrenheit é {f}º")

temperatura()
