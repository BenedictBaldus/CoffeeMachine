Latte = 5.0
Espresso =  3.0
Cappuccino =  4.5
print("Latte",Latte,"€",  "\nEspresso",Espresso,"€", "\nCappuccino",Cappuccino,"€")

while True:
  
  print("Bitte ein Getränk auswählen oder für abbruch 'ausschalten' eingeben\n  ")

  eingabe = input()

  if eingabe == "Latte":
    print("Hier ist der Latte")
    continue
  elif eingabe == "Espresso":
    print("Hier ist der Espresso")
    continue
  elif eingabe == "Cappuccino":
    print("Hier ist der Cappuccino")
    continue
  elif eingabe == "ausschalten":
    print("Kaffeemaschiene wird ausgeschaltet")
    break
  else:
    print("Fehlerhafte Eingabe, bitte erneut probieren")
    continue

  
