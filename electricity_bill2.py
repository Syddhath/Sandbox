TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff = int(input("Which tariff? 11 or 31?"))
while tariff != 11 and tariff !=31:
    if tariff == 11:
        tariff= TARIFF_11
    else:
        tariff= TARIFF_31

usage = float(input("Enter daily use in kWh"))
days = int(input("Enter number of days in billing period"))

callBill = tariff * usage * days

print("Estimated bill:", callBill)




