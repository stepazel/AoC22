text = open('commands', 'r')

storage = {
    1: ['W', 'R', 'F'],
    2: ['T', 'H', 'M', 'C', 'D', 'V', 'W', 'P'],
    3: ['P', 'M', 'Z', 'N', 'L'],
    4: ['J', 'C', 'H', 'R'],
    5: ['C', 'P', 'G', 'H', 'Q', 'T', 'B'],
    6: ['G', 'C', 'W', 'L', 'F', 'Z'],
    7: ['W', 'V', 'L', 'Q', 'Z', 'J', 'G', 'C'],
    8: ['P', 'N', 'R', 'F', 'W', 'T', 'V', 'C'],
    9: ['J', 'W', 'H', 'G', 'R', 'S', 'V']
}

while True:
    line = text.readline()
    if not line:
        break

    count = int(line[5])
    source_stack = int(line[12])
    target_stack = int(line[17])

    # for i in range(storage[4].count(), )

    print('hmm')


# Presouvam je z konce na konec po jednom, tj. tak jak to zapisuji je dobre (to pismenko, oc je nahore, je konec)
# Tj. presouvam vzdycky horni (posledni)
