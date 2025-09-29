class Teclado:
    def __init__(self):
        pass

    def ligar_teclado(self):
        print("Teclado ativado.")

class Mouse:
    def __init__(self):
        pass

    def ligar_mouse(self):
        print("Mouse ativado.")

class Monitor:
    def __init__(self):
        pass

    def ligar_monitor(self):
        print("Monitor ativado")

class Computador:
    def __init__(self):
        self.teclado = Teclado()
        self.mouse = Mouse()
        self.monitor = Monitor()

    def ligar_computador(self):
        self.teclado.ligar_teclado()
        self.mouse.ligar_mouse()
        self.monitor.ligar_monitor()

    def __str__(self):
        return f"O computador está ligado."
    
computador = Computador()

computador.ligar_computador()

print(computador)