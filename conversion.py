while True:
 answer=input("Do you wanna convert some units! If no then type 'n' But If yes then what do you wanna convert with? Type one of the first letters in lowercase of the units to convert them (1. Celsius to Fahrenheit = c or f 2. Miles to Km = m or k):")
 if answer.lower()=='c':
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
    if answer.lower()=='f':
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


 if answer.lower()=='m':
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
 else:
   if answer.lower()=='k':
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
