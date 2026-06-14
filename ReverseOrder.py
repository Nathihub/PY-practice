
Count = int(input("Enter a number to count its digits: "))
digit = 0
while Count > 0:
    Count = Count // 10
    digit = digit + 1
print("The number of digits in the given number is: ", digit)