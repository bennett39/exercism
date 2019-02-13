class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ','')

    def is_valid(self):
        if len(self.card_num) < 2: 
            return False
        for c in self.card_num:
            if not c.isdigit():
                return False

        total = 0
        for i in range(len(self.card_num)):
            digit = int(self.card_num[-i-1])
            if i % 2 == 1: 
                if digit > 4: total += digit * 2 - 9
                else: total += digit * 2
            else: 
                total += digit

        if total % 10 == 0:
            return True
        return False
