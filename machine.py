Latte = 5.0
Espresso =  3.0
Cappuccino =  4.5
print("Latte",Latte,"€",  "\nEspresso",Espresso,"€", "\nCappuccino",Cappuccino,"€")

while True:
  
  print("Bitte ein Getränk auswählen oder für abbruch 'ausschalten' eingeben\n  ")

  eingabe = input()

  if eingabe == "Latte" or eingabe == "latte":
    print("Hier ist der Latte")
    continue
  elif eingabe == "Espresso" or eingabe == "espresso":
    print("Hier ist der Espresso")
    continue
  elif eingabe == "Cappuccino" or eingabe == "cappuccino":
    print("Hier ist der Cappuccino")
    continue
  elif eingabe == "ausschalten" or eingabe == "Ausschalten":
    print("Kaffeemaschiene wird ausgeschaltet")
    break
  else:
    print("Fehlerhafte Eingabe, bitte erneut probieren")
    continue

  
