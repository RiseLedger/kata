digits = [
    [" _ ", "| |", "|_|"], # 0
    ["   ", " | ", " | "], # 1
    [" _ ", " _|", "|_ "], # 2
    [" _ ", " _|", " _|"], # 3
    ["   ", "|_|", "  |"], # 4
    [" _ ", "|_ ", " _|"], # 5
    [" _ ", "|_ ", "|_|"], # 6
    [" _ ", "  |", "  |"], # 7
    [" _ ", "|_|", "|_|"], # 8
    [" _ ", "|_|", " _|"]  # 9
];

user_input = raw_input()
result = ""
depth = 0

while depth < 3:
    result = result + "\n"

    for i in user_input:
        result = result + digits[int(i)][depth]

    depth += 1

print result
