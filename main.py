class Materie:
    def __init__(self, nume):
        self.nota = None
        self.nume = nume

    def setNota(self):
        self.nota = float(input("Nota " + self.nume + ": "))

    def getNota(self):
        if self.nume == "Bacalaureat":
            return self.nota
        return 0.5 * self.nota


def calc():
    return 0.2 * bac.getNota() + 0.8 * (mate.getNota() + info.getNota())


if __name__ == '__main__':
    mate = Materie("Matematica")
    info = Materie("Informatica")
    bac = Materie("Bacalaureat")

    mate.setNota()
    info.setNota()
    bac.setNota()

    print("{:.2f}".format(calc()))
