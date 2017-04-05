cc = 5
lc = 10
tvc = 15
shc = 3

def total_Cost(c, l, tv):
    total = (c * cc)+(l * lc)+(tv * tvc)
    totalQty = c + l + tv
    print("Total cost =", total)
    if total > 100:
        discount = total * 0.1
        print("User's discount is:",total)
    else:
        print("Shipping to fees will be applied. Grand total is:", total + (totalQty * shc))

def getQty(message):
    qty = int(input(message))
    while qty < 0:
        print ("Error. Input must be more than 0")
        qty = int(input(message))
    return qty

def main():
    c = getQty("How many cellphone do you want?")
    l = getQty("How many laptop do you want?")
    tv = getQty("How many tv do you want?")
    print("Number of cellphones:", c)
    print("Number of laptops:", l)
    print("Number of tv:", tv)
    total_Cost(c, l, tv, shc)
main()