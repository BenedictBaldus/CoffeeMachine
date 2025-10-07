Latte = 5.0
Espresso =  3.0
Cappuccino =  4.5
#print("Latte",Latte,"€",  "\nEspresso",Espresso,"€", "\nCappuccino",Cappuccino,"€")

coffe = { "Latte" : 5.0,
          "Espresso" : 3.0,
          "Cappuccino" : 4.5 }

for drink,preis in coffe.items():
  print(drink, "kostet", preis,"€")


summe = 0


while True:
  eingabe_coins = []
  print("\nBitte ein Getränk auswählen oder für das Ausschalten der Maschine 'off' eingeben\n  ")
  eingabe = input()

  if eingabe == "Latte" or eingabe == "latte":
    print(coffe.get("Latte"))
    print("Werfen Sie bitte das Geld ein.")
    
    while sum(eingabe_coins)<coffe.get("Latte"):
      eingabe_coins.append(float(input()))
      print(sum(eingabe_coins))


    print("Hier ist der Latte")
    continue
  elif eingabe == "Espresso" or eingabe == "espresso":
    print("Hier ist der Espresso")
    continue
  elif eingabe == "Cappuccino" or eingabe == "cappuccino":
    print("Hier ist der Cappuccino")
    continue
  elif eingabe == "off" or eingabe == "Off":
    print("Kaffeemaschiene wird ausgeschaltet")
    break
  else:
    print("Fehlerhafte Eingabe, bitte erneut probieren")
    continue

  
