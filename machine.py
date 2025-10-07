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

akzeptiere_muenzen = [0.1, 0.2, 0.5, 1.0, 2.0]
  

def ausgabe(drink):
  print("Werfen Sie bitte das Geld ein.")
  price = coffe[drink]["Preis"]

  while sum(eingabe_coins)<price:
      while True:
        temp_eingabe = float(input())
        
        if temp_eingabe in akzeptiere_muenzen:                                                                      #Prüfen ob die eingegebenen Münzen akzeptiert werden
          eingabe_coins.append(temp_eingabe)                                                                            
          print(f"Es wurden {round(sum(eingabe_coins),2)}€ eingeworfen.")

          if(sum(eingabe_coins)<price):                                                                                 #Prüfen ob die eingeworfenen Münzen zu wenig sind
            print("Das eingeworfene Geld reicht nicht aus, bitte mehr Geld einwerfen")
          elif(sum(eingabe_coins)>price):                                                                               #Prüfen ob die eingeworfenen Münzen zu viel sind
            rueckgeld(rueckgeld,price)
            break
          else:
            break 

        else:
          print("Ungültige Münze, es werden nur 0.1,0.2,0.5,1 oder 2 Euro Münzen akzeptiert.")                          #Ausgabe das ungültige Münzen eingeworfen wurden
          continue

def rueckgeld(rueckgeld,price):
  rueckgeld=round(sum(eingabe_coins)-price, 2)
  print(f"Sie bekommen {rueckgeld}€ Rückgeld")
  while rueckgeld>0:
    if rueckgeld>= 2.0:
      rueckgeld = round(rueckgeld -2.0, 2)
      print("Es werden 2.0€ ausgegeben")
    elif rueckgeld>=1.0:
      rueckgeld = round(rueckgeld -1.0, 2)
      print("Es werden 1.0€ ausgegeben")
    elif rueckgeld>=0.5:
      rueckgeld = round(rueckgeld -0.5, 2)
      print("Es werden 0.5€ ausgegeben")
    elif rueckgeld>=0.2:
      rueckgeld = round(rueckgeld -0.2, 2)
      print("Es werden 0.2€ ausgegeben")
    elif rueckgeld>=0.1:
      rueckgeld = round(rueckgeld -0.1, 2)
      print("Es werden 0.1€ ausgegeben")


while True:
  eingabe_coins = []
  count = 1
  for drink,preis in coffe.items():
    print(f"{count}: {drink} kostet {preis["Preis"]}€")
    count+=1
  print("\nBitte ein Getränk auswählen oder für das Ausschalten der Maschine 'off' eingeben\n  ")
  eingabe = input()
  if eingabe.lower() == "off":
    print("Kaffeemaschiene wird ausgeschaltet")
    break

  match eingabe:
    case "1":
      ausgabe("Latte")
      print("Der Latte wird ausgegeben")
    case "2":
      ausgabe("Espresso")
      print("Der Espresso wird ausgegeben")
    case "3":
      ausgabe("Cappucino")
      print("Der Cappuccino wird ausgegeben")
    case _:
      print("Fehlerhafte Eingabe, bitte erneut probieren")
      continue

  
  
