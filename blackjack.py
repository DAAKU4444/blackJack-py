#-blackJack -singleRound
from random import *

ctr1, ctr2 = 0, 0


while True:
    itr = input('start game(y/n)').lower()


    if itr=='n':
        break

    elif itr == 'y':
        p1 = input('enter name, player1')
        p2 = input('enter name, player2')
        
        print()


        while win == 0:
            
            print(p1,':',ctr1,' | ', p2,':',ctr2)
            pMove = input(p1,' (h)it or (p)ass?').lower()
            


      








        



