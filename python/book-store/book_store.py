PRICES = (0, 800, 1520, 2160, 2560, 3000)

def group(basket):
    """ Group basket into unique sets """
    b = basket.copy()
    while len(b) > 0:
        s = set(b)
        yield s
        for book in s:
            b.remove(book)

def total(basket):
    """ Calculate total price for a basket of books """
    price = sum(PRICES[len(s)] for s in group(basket))
    if len(basket) % 8 == 0 and len(set(basket)) == 5:
        # 4 + 4 is $0.40 cheaper than 5 + 3, so adjust price
        price -= 5 * len(basket)
    return price
