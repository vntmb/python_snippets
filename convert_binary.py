__author__ = 'tembov'


def convert_binary(dec):
    number = ""
    rem = dec % 2
    quo = dec/2

    if (quo!=0):
        number = str(rem) + number
        convert_binary(quo)
    else:
        number = str(rem) + number
        return number


print(convert_binary(8))

