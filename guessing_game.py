#this is a short programme like a game of number guessing , may be u like it ( '_' ).

print("                                      THIS IS A GAME OF GUESSING                                                ")
print("          You have to guess a Number which is multiple of 3 , and it will be in between 1 - 100                 ")

import random as r
while True:
    PC_choice = 3*r.randint(0, 33)

    a = PC_choice + r.randint(0,5)
    b = PC_choice - r.randint(0,5)
    print('The random number is greater than{} and less than{}'.format(b,a))
    User_choice = int(input("Enter your guessing number-->"))
    if User_choice is PC_choice:
        print('YOU GUESSED IT CORRECTLY')
        print('YOU ARE AN AVENGER NOW.')
    if User_choice%3 != 0:
        print("YOU FOOL , THIS IS NOT AN MULTIPLE OF THREE, GO AND LEARN TABLE FIRST")
    else:
        print('YOU ARE WRONG')
    print("if You want to play more, ENTER *piya maange more* and if not then ENTER *bss ho gya* ")
    c = input()
    if c == "bss ho gya":
        break


print("THANK YOU FOR USING THIS PROGRAMME.")
