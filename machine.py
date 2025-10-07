def ausgabe(drink):
  print(coffe[drink]["Preis"])
  print("Werfen Sie bitte das Geld ein.")
  price = coffe[drink]["Preis"]

  while sum(eingabe_coins)<price:
      while True:
        temp_eingabe = float(input())

        if temp_eingabe == 0.1 or temp_eingabe == 0.2 or temp_eingabe == 0.5 or temp_eingabe == 1 or temp_eingabe == 2: #Prüfen ob die eingegebenen Münzen akzeptiert werden
          eingabe_coins.append(temp_eingabe)                                                                            
          print("Die Summe ist",sum(eingabe_coins))

          if(sum(eingabe_coins)<price):                                                                                 #Prüfen ob die eingeworfenen Münzen zu wenig sind
            print("Das eingeworfene Geld reicht nicht aus, bitte mehr Geld einwerfen")
          elif(sum(eingabe_coins)>price):                                                                               #Prüfen ob die eingeworfenen Münzen zu viel sind
            rueckgeld=sum(eingabe_coins)-price
            print("Es wurde zuviel gezahlt, es werden",rueckgeld,"€ ausgegeben")
            break
          else:
            break 

        else:
          print("Ungültige Münze, es werden nur 0.1,0.2,0.5,1 oder 2 Euro Münzen akzeptiert.")                          #Ausgabe das ungültige Münzen eingeworfen wurden
          continue


coffe = { "Latte" : {
            "Preis" : 5.0,
            "Water" : 0,
            "Coffe" : 0,
            "Oatmilk": 0
          },
          "Espresso" : {
            "Preis" : 3.0,
            "Water" : 0,
            "Coffe" : 0,
            "Oatmilk": 0
          },
          "Cappuccino" : {
            "Preis" : 4.5,
            "Water" : 0,
            "Coffe" : 0,
            "Oatmilk": 0
          } }

for drink,preis in coffe.items():
  print(drink, "kostet", preis["Preis"],"€")

while True:
  eingabe_coins = []
  print("\nBitte ein Getränk auswählen oder für das Ausschalten der Maschine 'off' eingeben\n  ")
  eingabe = input()

  if eingabe == "Latte" or eingabe == "latte":
    ausgabe("Latte")
    print("Der Latte wird ausgegeben")
    continue
  elif eingabe == "Espresso" or eingabe == "espresso":
    ausgabe("Espresso")
    print("Der Espresso wird ausgegeben")
    continue
  elif eingabe == "Cappuccino" or eingabe == "cappuccino":
    ausgabe("Cappucino")
    print("Der Cappuccino wird ausgegeben")
    continue
  elif eingabe == "off" or eingabe == "Off":
    print("Kaffeemaschiene wird ausgeschaltet")
    break
  else:
    print("Fehlerhafte Eingabe, bitte erneut probieren")
    continue

  
