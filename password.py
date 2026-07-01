import random
list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
list2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numlist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
Password = ""
for i in range(2):
    Password += random.choice(list)
    Password += random.choice(numlist)
    Password += random.choice(list2)
print("The password is: ",Password)