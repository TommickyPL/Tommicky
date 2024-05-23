import random

logo = '''
 __    __    ___  _        __   ___   ___ ___    ___                                   
                                         
  ____  __ __    ___  _____ _____ ____  ____    ____       ____   ____  ___ ___    ___ 
 /    ||  |  |  /  _]/ ___// ___/|    ||    \  /    |     /    | /    ||   |   |  /  _]
|   __||  |  | /  [_(   \_(   \_  |  | |  _  ||   __|    |   __||  o  || _   _ | /  [_ 
|  |  ||  |  ||    _]\__  |\__  | |  | |  |  ||  |  |    |  |  ||     ||  \_/  ||    _]
|  |_ ||  :  ||   [_ /  \ |/  \ | |  | |  |  ||  |_ |    |  |_ ||  _  ||   |   ||   [_ 
|     ||     ||     |\    |\    | |  | |  |  ||     |    |     ||  |  ||   |   ||     |
|___,_| \__,_||_____| \___| \___||____||__|__||___,_|    |___,_||__|__||___|___||_____|

__    __    ___  _        __   ___   ___ ___    ___      
                                                                                      
'''
print(logo)

def game():

    random_0_100 = random.randint(0,100)

    print('I think of a number between 1 and 100')

    user_dif = input('Coose a difficulty, Type "easy" or "hard" : ')
    user_life = 0
    mistakes_count = 0

    if user_dif == 'easy':
        user_life = 10
    elif user_dif == 'hard':
        user_life = 5

    player_win = False
    while not player_win == True:
        print(f'lives remaining :{user_life - mistakes_count}')
        number_guessed = int(input('Type your guess: '))
        
        if random_0_100 > number_guessed:
            print(f'the number is higher than {number_guessed}')
            mistakes_count +=1
        elif random_0_100 < number_guessed:
            print(f'the number is lower than {number_guessed}')
            mistakes_count +=1
        elif random_0_100 == number_guessed:
            print('Well done you Win!!!!!')
            player_win = True
        if mistakes_count == user_life:
            player_win = True
            print('You loose')
           


while True:
    play_again = input('Do you like to play? press "y" : ')
    if play_again =='y':
        game()
    
                
    
