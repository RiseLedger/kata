from random import randint

class ISBN:

    def __init__(self):
        pass

    def isValid(self, str):
        total = float()
        for i in range(10, 1, -1):
            total = total + i * float( str[ abs( 10 - i ) ] )

        if str[-1] == 'X':
            total = total + 10
        else:
            total = total + float( str[-1] )

        return  ( total / 11 ).is_integer()

    def isInvalid(self, str):
        return not self.isValid(str)

    def generate(self):
        isbn = ""
        total = int()
        to_add = 11

        for i in range(10,1,-1):
            generated_number = randint(0, 9)
            isbn = isbn + str( generated_number )
            total = total + ( i * generated_number )

        to_add = to_add - (total % 11)

        if to_add == 11:
            isbn = isbn + '0'
        elif to_add == 10:
            isbn = isbn + 'X'
        else:
            isbn = isbn + str( to_add )

        return isbn


isbn = ISBN()
print isbn.isValid('0747532699')
print isbn.isValid('156881111X')

generated_isbn = isbn.generate()
print 'Generated ISBN: ' + generated_isbn
print isbn.isValid( generated_isbn )
