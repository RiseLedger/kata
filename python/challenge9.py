import random
pieces = ['O', 'I', 'S', 'Z', 'L', 'J', 'T']
sequence = ''

for x in range(50):
    currentIndex = x % len(pieces)

    if currentIndex == 0:
        random.shuffle(pieces)

    sequence += pieces[currentIndex]

print sequence
