import os

col = os.get_terminal_size().columns
lines = os.get_terminal_size().lines


def header():
    pre = "Contador Izq: 0"
    post = "Contador Der: 0"

    print(pre + " " * (col - len(pre) - len(post) - 2) + post)


def cuadricula():
    print("╔" + "═" * (col - 3) + "╗")

    for i in range(lines - 8):
        print("║" + "*" * (col - 3) + "║")

    print("╚" + "═" * (col - 3) + "╝")


def footer(registros):

    for registro in registros:
        print(registro)


def main():
    header()
    cuadricula()
    footer(["Registro 1", "Registro 2", "Registro 3", "Registro 4"])


main()
