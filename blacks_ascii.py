def get_number():
    while True:
        try:
            upper_number = int(input("Enter a number: "))
        except ValueError:
            print("invalid int")
            continue
        else:
            return upper_number

number = 'number'
character = 'char'
print("{:^8}".format(number, character))
for i in range(0, get_number()):
    print ("{:^8d} {:^8s}".format(i, chr(i)))