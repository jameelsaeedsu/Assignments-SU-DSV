year = int(input("Year: "))
while not int(year) in range(1583,10000):
    print("Out of allowed range 1583 to 9999")
    year = int(input("Year: "))

month = int(input("Month: "))
while not int(month) in range (1,13):
    print("Out of allowed range 1 to 12")
    month = int(input("Month: "))
    

while True:
    day = int(input("Day: "))
#Upprepa det här tills det kommer en break där det avbryts

    if month in [4, 6, 9, 11] and day >= 31:
        print("Out of allowed range 1 to 30")
        
    elif month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        print("Out of allowed range 1 to 31")

    elif month in [2]:
        if (year % 400) == 0 or ((year % 4) == 0 and (year % 100) != 0):
            if day > 29:
                print("Out of allowed range 1 to 29")
            
            else:
                break
        else:
            if day > 28:
                print("Out of allowed range 1 to 28")
                
            else:
                break
    else:
        break
#break = avbryter loopen

if month == 1 or month == 2:
    month += 12
    year -= 1

#Weekday formula
weekday = (day + 13*(month+1)//5 + year + year//4 - year//100 + year//400) % 7

if weekday  == 0:
    print("It is a Saturday")
elif weekday == 1:
    print("It is a Sunday")
elif weekday == 2:
    print("It is a Monday")
elif weekday == 3:
    print("It is a Tuesday")
elif weekday == 4:
    print("It is a Wednesday")
elif weekday == 5:
    print("It is a Thursday")
elif weekday == 6:
    print("It is a Friday")
