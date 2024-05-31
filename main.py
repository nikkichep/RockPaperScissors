 # complete game of rock, paper, scissors
player1 = 'paper'
player2 = 'scissors'

if player1 == player2:
   print('Its a tie')



if player1 == 'rock':
    if player2 == 'paper':
     print('player 2 won')
    elif player2 == 'scissors':
       print('player 1 won')

if player1 == 'paper':
    if player2 == 'rock':
     print('player 1 won')
    elif player2 == 'scissors':
     print('player 2 won')
if player1 == 'scissors':
    if player2 == 'rock':
     print('player 2 won')
    elif player2 == 'paper':
     print('player 1 won')