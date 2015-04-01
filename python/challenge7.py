import re

inputData = raw_input('What is the text of verse you want to search?\n\n')

book = open('../extra/challenge7_text.txt')
lines = book.read().split('\n')
i = 0
isVerse = False
found = False
verse = '\n'

for line in lines:
    m = re.search('^\s{2}[a-zA-Z].+', line)

    if isVerse:
        verseLine = re.search('^\s{4}[a-zA-Z].+', line)

        if verseLine:
            verse = verse + line + '\n'
            if inputData in line:
                found = True
        else:
            if found:
                break

            isVerse = False
            verse = '\n'

    if m:
        isVerse = True

    i += 1

print verse
