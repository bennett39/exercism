def check_luhn(number):
    total = 0
    for i in range(len(number)):
        digit = int(number[-i-1])
        if i % 2 == 1: 
            total += double_digit(digit)
        else: 
            total += digit
    if total % 10 == 0:
        return True
    return False


def double_digit(digit):
    if digit > 4: return digit * 2 - 9
    return digit * 2


class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ','')

    def is_valid(self):
        if len(self.card_num) < 2: 
            return False
        for c in self.card_num:
            if not c.isdigit():
                return False
        return check_luhn(self.card_num)
