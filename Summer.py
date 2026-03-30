list = ["Ben", "Vihaan", "Yuvan", "Noah", "Aarav", "Ethan", "Mason", "Logan", "Lucas", "Alex","Rohan"]
name = input("Enter your name to check if it is in the party list: ")
if name in list:
    print(name, "is in the party list and can attend the party.")
else:
    print(name, "is not in the party list and cannot attend the party.")
