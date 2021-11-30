addresses = [
    "12/45 Elm street",
    '34/56 Clark street',
    '56,77 maple street',
    '17/45 Elm street'

]
street = 'maple street'
for i in addresses:
    if street in i:
        print(i)
