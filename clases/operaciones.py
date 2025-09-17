class Operaciones:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = ""

    def leerNumeros(self):
        while True:
            try:
                self.num1 = int(input("Número 1: "))
                break
            except ValueError:
                print("Número inválido. Intenta de nuevo.")

        while True:
            try:
                self.num2 = int(input("Número 2: "))
                break
            except ValueError:
                print("Número inválido. Intenta de nuevo.")

    def sumar(self):
        r = self.num1 + self.num2
        self.resultado = f"La suma de {self.num1} + {self.num2} es igual a {r}"
        return r

    def restar(self):
        r = self.num1 - self.num2
        self.resultado = f"La resta de {self.num1} - {self.num2} es igual a {r}"
        return r

    def multiplicar(self):
        r = self.num1 * self.num2
        self.resultado = f"La multiplicación de {self.num1} * {self.num2} es igual a {r}"
        return r

    def dividir(self):
        if self.num2 == 0:
            self.resultado = "Error: No se puede dividir entre cero."
            return None
        r = self.num1 / self.num2
        self.resultado = f"La división de {self.num1} / {self.num2} es igual a {r}"
        return r

    def mostrarResultado(self):
        print(self.resultado)
        