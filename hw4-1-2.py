# Author: ALJ (AMDG) 10/7/20

#Only input the number of cards drawn, input zero for cards not drawn

card1 = int(input("What is the value of your first card? "))
card2 = int(input("What is the value of your second card? "))
card3 = int(input("What is the value of your third card? "))
card4 = int(input("What is the value of your fourth card? "))
card5 = int(input("What is the value of your fifth card? "))
card_value = (card1 + card2 + card3 + card4 + card5)

if card_value > 21:
    print("You bust!")
else:
    print("You're safe.")