words = raw_input().split()

for c in words[0]:
    if c in words[1]:
        words[0] = words[0].replace(c, '', 1)
        words[1] = words[1].replace(c, '', 1)

if len(words[0]) > len(words[1]):
    print 'First word win, Answer: ' + words[0] + words[1]
elif len(words[0]) < len(words[1]):
    print 'Second word win, Answer: ' + words[0] + words[1]
else:
    print 'The game is tie, Answer: ' + words[0] + words[1]
