class CarryAdding:

    rawinput = None
    numbers = None
    total = None
    max_width = 0
    line_length = 0
    compute_list = None

    def __init__(self, numbers):
        self.rawinput = numbers
        self.numbers = [n.strip() for n in numbers.split("+")]
        self.total = sum(int(x) for x in self.numbers)

        self.init()

    def init(self):
        self.setMaxWidth()
        self.printFormattedAnswer()

    def setMaxWidth(self):
        for number in self.numbers:
            if len(number) > self.max_width:
                self.max_width = len(number)

        self.line_length = self.max_width + 3
        self.compute_list = [0] * self.max_width

    def computeCarry(self):
        carryToAdd = 0;
        carry_output = ''
        for number in self.numbers:
            reverse_number = number[::-1]
            for i in range(0, self.max_width):
                if i < len(reverse_number):
                    self.compute_list[i] = self.compute_list[i] + int(reverse_number[i])

        i = 0
        for n in self.compute_list:
            if len(str(n)) > 1:
                carryToAdd = int( str(n)[:-1] )
                carry_output = carry_output + str(n)[:-1]

                try:
                    self.compute_list[i + 1] = self.compute_list[i + 1] + carryToAdd
                except:
                    pass
            else:
                carry_output = carry_output + ' '

            i += 1

        return ' ' + ''.join(carry_output)

    def printFormattedAnswer(self):
        carry_result = self.computeCarry()
        print '\n'
        for number in self.numbers:
            print number.rjust(self.line_length, ' ')

        self.addSeparator()
        print str(self.total).rjust(self.line_length, ' ')
        self.addSeparator()
        print carry_result[::-1].rjust(self.line_length, ' ')

    def addSeparator(self):
        print ('-'*self.max_width).rjust(self.line_length, ' ')


if __name__ == '__main__':
    CarryAdding( raw_input("Give me the numbers to add:") )
