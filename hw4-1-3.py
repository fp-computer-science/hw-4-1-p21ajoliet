# Author: ALJ (AMDG) 10/7/20

x = int(input("What number are you thinking of? "))

if x % 2 == 0 and x % 3 == 0 and x % 5 == 0:
    print("The number you are thinking of is divisable by two, three, and five.")
elif x % 2 == 0 and x % 3 == 0:
    print("The number you are thinking of is divisable by two and three, but not divisable by five.")
elif x % 2 == 0 and x % 5 == 0:
    print("The number you are thinking of is divisable by two and five, but not divisable by three.")
elif x % 3 == 0 and x % 5 == 0:
    print("The number you are thinking of is divisable by three and five, but not divisable by two.")
elif x % 2 == 0:
    print("The number you are thinking of is divisable by two, but not divisable by three and five.")
elif x % 3 == 0:
    print("The number you are thinking of is divisable by three, but not divisable by two and five.")
elif x % 5 == 0:
    print("The number you are thinking of is divisable by five, but not divisable by two and three.")
else:
    print("The number you are thinking of is not divisable by two, three, or five.")