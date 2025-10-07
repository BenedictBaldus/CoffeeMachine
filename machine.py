coffe = { "Latte" : {                 #Preis in €, Wasser in ml, Coffe in mg, Oatmilk in ml
            "Preis" : 5.0,
            "Water" : 100,
            "Coffe" : 25,
            "Oatmilk": 250
          },
          "Espresso" : {
            "Preis" : 3.0,
            "Water" : 50,
            "Coffe" : 20,
            "Oatmilk": 0
          },
          "Cappuccino" : {
            "Preis" : 4.5,
            "Water" : 250,
            "Coffe" : 25,
            "Oatmilk": 100
          } }

for drink,preis in coffe.items():
  print(drink, "kostet", preis["Preis"],"€")

akzeptiere_muenzen = [0.1, 0.2, 0.5, 1.0, 2.0]


def ausgabe(drink):
  print(coffe[drink]["Preis"])
  print("Werfen Sie bitte das Geld ein.")
  price = coffe[drink]["Preis"]

  while sum(eingabe_coins)<price:
      while True:
        temp_eingabe = float(input())
        
        if temp_eingabe in akzeptiere_muenzen:                                                                      #Prüfen ob die eingegebenen Münzen akzeptiert werden
          eingabe_coins.append(temp_eingabe)                                                                            
          print("Die Summe ist",round(sum(eingabe_coins),2))

          if(sum(eingabe_coins)<price):                                                                                 #Prüfen ob die eingeworfenen Münzen zu wenig sind
            print("Das eingeworfene Geld reicht nicht aus, bitte mehr Geld einwerfen")
          elif(sum(eingabe_coins)>price):                                                                               #Prüfen ob die eingeworfenen Münzen zu viel sind
            rueckgeld=round(sum(eingabe_coins)-price, 2)
            print(rueckgeld)
            while rueckgeld>0:
              match rueckgeld:
                case g if rueckgeld>= 2.0:
                  rueckgeld = round(rueckgeld -2.0, 2)
                  print("Es werden 2.0€ ausgegeben")
                case g if rueckgeld>=1.0:
                  rueckgeld = round(rueckgeld -1.0, 2)
                  print("Es werden 1.0€ ausgegeben")
                case g if rueckgeld>=0.5:
                  rueckgeld = round(rueckgeld -0.5, 2)
                  print("Es werden 0.5€ ausgegeben")
                case g if rueckgeld>=0.2:
                  rueckgeld = round(rueckgeld -0.2, 2)
                  print("Es werden 0.2€ ausgegeben")
                case g if rueckgeld>=0.1:
                  rueckgeld = round(rueckgeld -0.1, 2)
                  print("Es werden 0.1€ ausgegeben")
            break
          else:
            break 

        else:
          print("Ungültige Münze, es werden nur 0.1,0.2,0.5,1 oder 2 Euro Münzen akzeptiert.")                          #Ausgabe das ungültige Münzen eingeworfen wurden
          continue




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

  
