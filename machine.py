import datetime
coffe = { "Latte Macchiato" : {                 #Preis in €, Wasser in ml, Coffe in mg, Oatmilk in ml
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
#Ressources
water = 2000 # in ml
grinder = 50 # in g
oatmilk = 1000 # in ml
einnahmen = 0
cashdrawer= {
"10 Cent" : 10,
"20 Cent" : 10,
"50 Cent" : 10,
"1 Euro" : 0,
"2 Euro" : 10,
}

akzeptiere_muenzen = [0.1, 0.2, 0.5, 1.0, 2.0]
  

def einwurf_muenzen(drink):
  print("Werfen Sie bitte das Geld ein.")
  price = coffe[drink]["Preis"]
  global einnahmen
  while sum(eingabe_coins)<price:
      while True:
        temp_eingabe = input()

        if(temp_eingabe.lower() == "abbruch"):
          print("Der Vorgang wird abgebrochen")
          rueckgeld(eingabe_coins,0)
          return
        else:
          temp_eingabe = float(temp_eingabe)

          if temp_eingabe == 2.0:
            cashdrawer.update({"2 Euro": cashdrawer["2 Euro"]+1})
            einnahmen += 2
          elif temp_eingabe == 1.0:
            cashdrawer.update({"1 Euro": cashdrawer["1 Euro"]+1})
            einnahmen += 1
          elif temp_eingabe == 0.5:
            einnahmen += 0.5
            cashdrawer.update({"50 Cent": cashdrawer["50 Cent"]+1})
          elif temp_eingabe == 0.2:
            cashdrawer.update({"20 Cent": cashdrawer["20 Cent"]+1})
            einnahmen += 0.2
          elif temp_eingabe == 0.1:
            cashdrawer.update({"10 Cent": cashdrawer["10 Cent"]+1})
            einnahmen += 0.1

          if temp_eingabe in akzeptiere_muenzen:                                                                      #Prüfen ob die eingegebenen Münzen akzeptiert werden
            eingabe_coins.append(temp_eingabe)                                                                            
            print(f"Es wurden {round(sum(eingabe_coins),2)}€ eingeworfen.")

            if(sum(eingabe_coins)<price):                                                                                 #Prüfen ob die eingeworfenen Münzen zu wenig sind
              print("Das eingeworfene Geld reicht nicht aus, bitte mehr Geld einwerfen. Oder für Abbrechen 'Abruch' eingeben")
            elif(sum(eingabe_coins)>price):                                                                               #Prüfen ob die eingeworfenen Münzen zu viel sind
              rueckgeld(rueckgeld,price)
              ressourcen(drink)
              break
            else:
              ressourcen(drink)
              break
          else:
            print("Ungültige Münze, es werden nur 0.1,0.2,0.5,1 oder 2 Euro Münzen akzeptiert.")                          #Ausgabe das ungültige Münzen eingeworfen wurden
            continue

def report():
  global einnahmen
  print(f"Wasser {water} ml")
  print(f"Milch {oatmilk} ml")
  print(f"Kaffe {grinder} g")
  
  print(f"Einnahmen {einnahmen} €\n")

  report_name = "report.txt"
  with open(report_name, "w") as datObj:
  #datObj = open(report_name, "w")
    datObj.write(f"Wasser: {water} ml\n")
    datObj.write(f"Milch: {oatmilk} ml\n")
    datObj.write(f"Kaffe: {grinder} mg\n")
    datObj.write(f"Einnahmen: {einnahmen} €\n")
  

def replenish():
  global water
  global grinder
  global oatmilk
  
  water = 2000 # in ml
  grinder = 500 # in g
  oatmilk = 1000 # in ml
  timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  with open("log.txt", "a") as datObj:
    datObj.write(f"{timestamp} Replenished\r\n")


def rueckgeld(rueckgeld,price):
  global einnahmen
  rueckgeld=round(sum(eingabe_coins)-price, 2)
  print(f"Sie bekommen {rueckgeld}€ Rückgeld")
  while rueckgeld>0:
    if rueckgeld>= 2.0 and cashdrawer["2 Euro"]>0:
      rueckgeld = round(rueckgeld -2.0, 2)
      cashdrawer.update({"2 Euro": cashdrawer["2 Euro"]-1})
      print("Es werden 2.0€ ausgegeben")
      einnahmen -=2
    elif rueckgeld>=1.0 and cashdrawer["1 Euro"]>0:
      rueckgeld = round(rueckgeld -1.0, 2)
      cashdrawer.update({"1 Euro": cashdrawer["1 Euro"]-1})
      einnahmen -=1
      print("Es werden 1.0€ ausgegeben")
    elif rueckgeld>=0.5 and cashdrawer["50 Cent"]>0:
      rueckgeld = round(rueckgeld -0.5, 2)
      cashdrawer.update({"50 Cent": cashdrawer["50 Cent"]-1})
      einnahmen -=0.5
      print("Es werden 0.5€ ausgegeben")
    elif rueckgeld>=0.2 and cashdrawer["20 Cent"]>0:
      rueckgeld = round(rueckgeld -0.2, 2)
      cashdrawer.update({"20 Cent": cashdrawer["20 Cent"]-1})
      einnahmen -=0.2
      print("Es werden 0.2€ ausgegeben")
    elif rueckgeld>=0.1 and cashdrawer["10 Cent"]>0:
      rueckgeld = round(rueckgeld -0.1, 2)
      cashdrawer.update({"10 Cent": cashdrawer["10 Cent"]-1})
      einnahmen -=0.1
      print("Es werden 0.1€ ausgegeben")
    else:
      print("Nicht genügend Rückgeld vorhanden")
      break

def ressourcen(drink):
  global water
  global oatmilk
  global grinder
  if((water-coffe[drink]["Water"])>0 and (oatmilk - coffe[drink]["Oatmilk"])>0 and (grinder - coffe[drink]["Coffe"])>0):
    water = water - coffe[drink]["Water"]
    oatmilk = oatmilk - coffe[drink]["Oatmilk"]
    grinder = grinder - coffe[drink]["Coffe"]
    print(f"\nDer {drink} wird ausgegeben\n ")
    
  else:
    print("\nBitte Ressourcen nachfüllen\n")

while True:
  eingabe_coins = []
  count = 1
  for drink,preis in coffe.items():
    print(f"{count}: {drink} kostet {preis["Preis"]}€")
    count+=1
  print("\nBitte ein Getränk auswählen oder für das Ausschalten der Maschine 'off'. Für den Report 'report' oder für das Nachfüllen 'replenish' ein. \n  ")
  eingabe = input()
  if eingabe.lower() == "off":
    print("Kaffeemaschiene wird ausgeschaltet")
    break
  elif eingabe.lower() == "report":
    report()
  elif eingabe.lower() == "replenish":
    replenish()

  match eingabe:
    case "1":
      drink = "Latte Macchiato"
      print(f"Es wurde der {drink} gewählt")
      einwurf_muenzen(drink)
      
    case "2":
      drink = "Espresso"
      print(f"Es wurde der {drink} gewählt")
      einwurf_muenzen(drink)
      
      
    case "3":
      drink = "Cappucino"
      print(f"Es wurde der {drink} gewählt")
      einwurf_muenzen(drink)
      
    case _:
      print("Fehlerhafte Eingabe, bitte erneut probieren\n")
      continue

  
  
