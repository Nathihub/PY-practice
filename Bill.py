units = int(input("Please enter the Number of Units you Consumed: "))

if(units < 50):
    bill = units * 2.60
    suncharge = 25
elif(units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    suncharge = 35
elif(units <= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    suncharge = 45
else:
    amount = 130 + 162.50 + ((units - 200) * 8.45)