print('''
                 _xAXAx_       /|  tsunami!!                         ^^
              _xAXXXXXXX=x.    / |  /
          _xAXXXXXXXXV        /x |_o/    ^^                         ^^
      _xAXXXXXXXXXXXA        /---| :
sjw XXXXXXXXXXXXXXXXXAx      '---_/_\_
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
''')
print("Welcome to Surfers Paradise!")
name = input("What's your name? ")
print(f"{name}, your mission is to catch the Barrel on a secret spot!!!")

wave = input("Wave coming! Which wave is it: Left, type 'Left', or Right, type 'Right'? ")
wave = wave.lower()

if wave == "right":
    wave_type = input("Barrel, type 'Barrel', or open face, type 'Open face'? ")
    wave_type = wave_type.lower()
    if wave_type == "barrel":
        barrel_type = input("Which kind of barrel? choose: 'Backdoor', 'Easy shape' or 'Airdrop slab' ")
        barrel_type = barrel_type.lower()
        if barrel_type == "backdoor":
            print(f"{name}, you was dropped-in by locals. You so hungry for waves, they said. You dead. Game over ;(")
        elif barrel_type == "easy shape":
            print(f"{name}, you was eaten by locals. Game over. ;(")
        elif barrel_type == "airdrop slab":
            print(f"{name} you WIN! Enjoy the Ride, Dude! ;)))")
        else:
            print(f"{name}, you was smashed on a dry reef. You dead. Game over. :(((")
    else:
        print(f"{name}, you caught a lip on your head. Smashed on a dry reef. You dead. Game over. :((")
else:
    print(f"{name}, you dropped-in a local guy. You dead. Game over. :(((")
