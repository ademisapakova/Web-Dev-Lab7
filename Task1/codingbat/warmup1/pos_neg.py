def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return (a < 0 < b) or (a > 0 > b)
