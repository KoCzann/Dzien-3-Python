haslo_poprawne = "Ninja2025"

while True:
    wpis = input("Podaj hasło: ")
    if wpis == haslo_poprawne:
        print("Hasło poprawne! Witamy.")
        break
    else:
        print("Złe hasło, spróbuj ponownie.")
    