Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
Power = 0
for i in range(1, Num2 + 1):
    Power = Num1 ** Num2
print("The power of", Num1, "raised to", Num2, "is", Power)
    