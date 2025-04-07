def tabla_asci():
    qty = 6
    for i in range(33, 255):
        print(str(i).ljust(4) + ":  " + chr(i), end="      ")
        if i % qty == 0:
            print()


tabla_asci()
