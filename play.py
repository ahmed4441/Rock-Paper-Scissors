def mode3():
    rules = {
    		"rock" : 'scissors',
    		"paper" : 'rock',
    		"scissors" : 'paper',
    	}
    ps = 0
    bs = 0
    botc = ['scissors','rock','paper']
    game = 1

    while game<6:
        i = game-1
        print('####### GAME {} #######'.format(game))
        player = input('your Turn: ').lower()
        bot = botc[i]
        if player not in rules or bot not in rules:
            print('rock paper scissors')
        else:
            bot = botc[i]
            if rules[player] == bot:
                print ('player wins')
                ps += 1
            elif player == bot:
                print ('Draw')
            else :
                print('Bot wins')
                bs += 1
            print(  'Player: {} - Bot: {}'.format(ps,bs)  )
            game += 1
            if i == 3 : i=0
    print('######### FINAL SCORE #########')
    print('Player: {} - Bot: {}'.format(ps,bs))
    if ps > bs:
        print('Player wins')
    elif ps == bs:
        print('Draw')
    else: print('Bot wins')
###############################
def mode0():
    rules = {
    		"rock" : 'scissors',
    		"paper" : 'rock',
    		"scissors" : 'paper',
    	}
    p1s = 0
    p2s = 0
    game = 1

    while game<6:

        print('####### GAME {} #######'.format(game))
        player1 = input('Player1 Turn: ').lower()
        player2 = input('Player2 turn: ').lower()
        if player1 not in rules or player2 not in rules:
            print('rock paper scissors')
        else:
            if rules[player1] == player2:
                print ('player1 wins')
                p1s += 1
            elif player1 == player2:
                print ('Draw')
            else :
                print('player2 wins')
                p2s += 1
            print(  'Player1: {} - Player2: {}'.format(p1s,p2s)  )
            game += 1
    print('######### FINAL SCORE #########')
    print('Player1: {} - Player2: {}'.format(p1s,p2s))
    if p1s > p2s:
        print('Player1 wins')
    elif p1s == p2s:
        print('Draw')
    else: print('Player2 wins')
#################################
def mode1():
    rules = {
    		"rock" : 'scissors',
    		"paper" : 'rock',
    		"scissors" : 'paper',
    	}
    ps = 0
    bs = 0
    game = 1

    while game<6:
        print('####### GAME {} #######'.format(game))
        player = input('your Turn: ').lower()
        bot = "rock"
        if player not in rules or bot not in rules:
            print('rock paper scissors')
        else:
            if rules[player] == bot:
                print ('player wins')
                ps += 1
            elif player == bot:
                print ('Draw')
            else :
                print('Bot wins')
                bs += 1
            print(  'Player: {} - Bot: {}'.format(ps,bs)  )
            game += 1
    print('######### FINAL SCORE #########')
    print('Player: {} - Bot: {}'.format(ps,bs))
    if ps > bs:
        print('Player wins')
    elif ps == bs:
        print('Draw')
    else: print('Bot wins')
#####################
def mode2():
    import random
    rules = {
    		"rock" : 'scissors',
    		"paper" : 'rock',
    		"scissors" : 'paper',
    	}
    ps = 0
    bs = 0
    botc = ['scissors','rock','paper']
    game = 1

    while game<6:

        print('####### GAME {} #######'.format(game))
        player = input('your Turn: ').lower()
        bot = random.choice(botc)
        if player not in rules or bot not in rules:
            print('rock paper scissors')
        else:

            if rules[player] == bot:
                print ('player wins')
                ps += 1
            elif player == bot:
                print ('Draw')
            else :
                print('Bot wins')
                bs += 1
            print(  'Player: {} - Bot: {}'.format(ps,bs)  )
            game += 1

    print('######### FINAL SCORE #########')
    print('Player: {} - Bot: {}'.format(ps,bs))
    if ps > bs:
        print('Player wins')
    elif ps == bs:
        print('Draw')
    else: print('Bot wins')
##################
choice = int(input("Choose mode number: (0 - 1 - 2 - 3)"))
if choice == 0 :
    mode0()
elif choice == 1:
    mode1()
elif choice == 2:
    mode2()
elif choice == 3:
    mode3()
