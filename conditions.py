print("Sprawdź czy jesteś pełnoletni")
age = int(input("Podaj swój wiek: "))
                
if age < 18:
    print("Nie jesteś pełnoletni")
elif age  == 18:
    print("Masz dokłądnie 18 lat")
else: 
    print("Wow! Jesteś pełnoletni")