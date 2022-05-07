while True:
 answer=input("Do you wanna convert some units! If no then type 'n' But If yes then what do you wanna convert with? Type the first five letters of the units in lowercase to convert them (1. Celsius to Fahrenheit = celsi or fahre 2. Miles to Kilometers = miles or kilom 3. Kilograms to Pounds = kilog or pound):")
 if answer.lower()=='celsi':
   answer=input("F° to C° or C° to F° (Type the letters in lowercase and in order of how you want to convert e.g. fc for F° to C°)")
   if answer.lower()=='cf':
     Celsius = int(input("How much celsius do you wanna convert?"))
     Fahrenheit = Celsius * 9 / 5 + 32
     print("Your initial", Celsius, "Celsius is now", Fahrenheit, "Fahrenheit!")
   else:
    if answer.lower()=='fc':
      Fahrenheit = int(input("How much Fahrenheit do you wanna convert?"))
      Celsius = (Fahrenheit - 32) * 5 / 9
      print("Your initial", Fahrenheit, "Fahrenheit is now", Celsius, "Celsius!")
    else:
      print("I did'nt get that. Please open up the script again and try again.")
      quit()
 else:
   if answer.lower()=='n':
    print("Bye!")
    quit()

   else:
    if answer.lower()=='fahre':
     answer=input("F° to C° or C° to F° (Type the letters in lowercase and in order of how you want to convert e.g. fc for F° to C°)")
     if answer.lower()=='cf':
      Celsius = int(input("How much celsius do you wanna convert?"))
      Fahrenheit = Celsius * 9 / 5 + 32
      print("Your initial", Celsius, "Celsius is now", Fahrenheit, "Fahrenheit!")
     else:
      if answer.lower()=='fc':
        Fahrenheit = int(input("How much Fahrenheit do you wanna convert?"))
        Celsius = (Fahrenheit - 32) * 5 / 9
        print("Your initial", Fahrenheit, "Fahrenheit is now", Celsius, "Celsius!")
      else:
        print("I did'nt get that. Please open up the script again and try again.")
        quit()


 if answer.lower()=='miles':
     answer=input("Kilometers to Miles or Miles to Kilometers (Type the letters in lowercase and in order of how you want to convert e.g. km for Kilometers to Miles)")
     if answer.lower()=='km':
       Kilometers = int(input("How many Kilometers do you wanna convert?"))
       Miles = Kilometers / 1.609344
       print("Your initial", Kilometers, "Kilometers is now", Miles, "Miles!")
     else:
      if answer.lower()=='mk':
        Miles = int(input("How many Miles do you wanna convert?"))
        Kilometers = Miles * 1.609344
        print("Your initial", Miles, "Miles is now", Kilometers, "Celsius!")
      else:
        print("I did'nt get that. Please open up the script again and try again.")
        quit()
 else:
   if answer.lower()=='kilom':
     answer=input("Kilometers to Miles or Miles to Kilometers (Type the letters in lowercase and in order of how you want to convert e.g. km for Kilometers to Miles)")
     if answer.lower()=='km':
       Kilometers = int(input("How many Kilometers do you wanna convert?"))
       Miles = Kilometers / 1.609344
       print("Your initial", Celsius, "Celsius is now", Fahrenheit, "Fahrenheit!")
     else:
      if answer.lower()=='mk':
        Miles = int(input("How many Miles do you wanna convert?"))
        Kilometers = Miles * 1.609344
        print("Your initial", Miles, "Miles is now", Kilometers, "Celsius!")
      else:
        print("I did'nt get that. Please open up the script again and try again.")
        quit()

 if answer.lower()=='kilog':
     answer=input("Kilograms to Pounds or Pounds to Kilograms (Type the letters in lowercase and in order of how you want to convert e.g. kp for Kilograms to Pounds)")
     if answer.lower()=='kp':
       Kilograms = int(input("How many Kilograms do you wanna convert?"))
       Pounds = Kilograms * 2.2046226218 
       print("Your initial", Kilograms, "Kilograms is now", Pounds, "Pounds!")
     else:
      if answer.lower()=='pk':
       Pounds = int(input("How many Pounds do you wanna convert?"))
       Kilograms = Pounds / 2.2046226218 
       print("Your initial", Pounds, "Pounds is now", Kilograms, "Kilograms!")
      else:
        print("I did'nt get that. Please open up the script again and try again.")
        quit()
 else:
  if answer.lower()=='pound':
   answer=input("Kilograms to Pounds or Pounds to Kilograms (Type the letters in lowercase and in order of how you want to convert e.g. kp for Kilograms to Pounds)")
   if answer.lower()=='kp':
    Kilograms = int(input("How many Kilograms do you wanna convert?"))
    Pounds = Kilograms * 2.2046226218 
    print("Your initial", Kilograms, "Kilograms is now", Pounds, "Pounds!")
   else:
    if answer.lower()=='pk':
      Pounds = int(input("How many Pounds do you wanna convert?"))
      Kilograms = Pounds / 2.2046226218 
      print("Your initial", Pounds, "Pounds is now", Kilograms, "Kilograms!")
    else:
     print("I did'nt get that. Please open up the script again and try again.")
     quit()
