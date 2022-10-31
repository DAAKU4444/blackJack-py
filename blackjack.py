#-blackJack -singleRound 
#author ~Daksh Thakur
from random import *



while True:  #main game loop

    print('\n','_'*20,' BLACKJACK ','_'*20)
    sPrompt = input('\n Start Game?(y/n)').lower()
      #________________start prompt________________
    if sPrompt=='n':
        break
   
   
    elif sPrompt == 'y':   
         #________________player and variable declaration____________
        
        cards = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        # Ace = 1, Jack = 11, Queen = 12, King = 13
        ctrPlayer = 0
        ctrDealer = 0
        scP = str(0)
        scD = str(0)
        winVar = 0  # 0 by default,1 for player win, 2 for dealer win, 3 for tie
        currentTurn = 1 # 1-player 2-dealer 3-either's blackjack
        
        
        p1 = input('\n enter name of the player : '.title())
        p2 = input('\n enter name of the dealer : '.title())
        print()
         


        while winVar == 0:
            #__________ game start loop_______________  
            
            while currentTurn == 1 :
                #___________player's turn________
                
                scP = str(ctrPlayer)
                scoreDis = ' '.join([p1,' : ',scP,' | ',p2,' : ',scD ])
                print(scoreDis,'\n','_'*20,'\n')
                
                      
                if ctrPlayer >21:
                    print(p1,' BUST!')
                    currentTurn = 0
                    winVar =2
                    continue

                elif ctrPlayer == 21:
                    
                    currentTurn = 3
                    continue
                    
                        
                pMove = input(p1+' (h)it or (p)ass?').lower()
                if pMove =='p':

                    currentTurn = 2
     
                elif pMove =='h':
                    deal = choice(cards)
                    ctrPlayer+= cards.index(deal) +1
                
                
            while currentTurn == 2 :    
                #_________dealer's turn_______ 
                
                scD = str(ctrDealer)
                scoreDis = ' '.join([p1,' : ',scP,' | ',p2,' : ',scD ])
                print(scoreDis,'\n','_'*20,'\n') 
                
                if ctrDealer >21:
                    print(p2,' BUST!')
                    currentTurn = 0
                    winVar =1
                    continue

                elif ctrDealer == 21:
                    
                    currentTurn = 3  
                    continue

                elif ctrDealer >ctrPlayer:
                    currentTurn = 0
                    winVar = 2
                    continue  


                pMove = input(p2+' (h)it or (p)ass?').lower()   
                if pMove =='p':
                    if ctrDealer < 17:
                        print('Dealer cannot pass before total is under 17'.title())
                    
                    else :
                        currentTurn = 1

                elif pMove =='h':
                    deal = choice(cards)
                    ctrDealer+= cards.index(deal) +1
                
                

            while currentTurn == 3:
                #_________in case of a blackjack___________

                if ctrPlayer == 21:
                    while winVar == 0:
                        scD = str(ctrDealer)
                        scoreDis = ' '.join([p1,' : ',scP,' | ',p2,' : ',scD ])
                        print(scoreDis,'\n','_'*20,'\n')
                
                        

                        pMove = input(p2+' (h)it for push : ').lower()
                        deal = choice(cards)
                        ctrDealer+= cards.index(deal) +1

                        if  ctrDealer == 21:
                            print('Its a Push!')
                            winVar = 3

                        elif ctrDealer > 21:
                            print('BlackJack for ',p1) 
                            winVar = 1

                        



                
                elif ctrDealer == 21:
                    while winVar == 0:
                        scP = str(ctrPlayer)
                        scoreDis = ' '.join([p1,' : ',scP,' | ',p2,' : ',scD ])
                        print(scoreDis,'\n','_'*20,'\n')
                
                        

                        pMove = input(p1+' (h)it for push : ').lower()
                        deal = choice(cards)
                        ctrPlayer+= cards.index(deal) +1

                        if  ctrPlayer == 21:
                            print('Its a Push! ')
                            winVar = 3

                        elif ctrPlayer > 21:
                            print('BlackJack for ',p2) 
                            winVar = 2
                        
                        

                currentTurn = 0    
            
            
            scD = str(ctrDealer)
            scP = str(ctrPlayer)
            scoreDis = ' '.join([p1,' : ',scP,' | ',p2,' : ',scD ])
            
            if currentTurn ==0:
                continue    

        if winVar == 1:
            print('^'*10)
            print(scoreDis)
            print(p1,' Wins!')

        elif winVar == 2:
            print('^'*10)
            print(scoreDis)
            print(p2,' Wins!')

        elif winVar == 3:
            print('^'*10)
            print(scoreDis)
            print('The Game is a Tie!')

        print('~'*20,'\n'*4)             








           


               


            







        
        



      








        



