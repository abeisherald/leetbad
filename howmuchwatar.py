input = [1,8,6,2,5,4,8,3,7]




def dowser(input):
    maxamount = 0
    for start in input:
        for nextstart in input:
            if start < nextstart:
                amount = start * input.index(nextstart)
            else:
                amount = (nextstart) * input.index(nextstart)
            if amount > maxamount:
                maxamount = amount
            else:
                continue
    print(maxamount)

dowser(input)