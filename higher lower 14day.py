import random
from data14day import data
from art14day import logo,vs
print(len(data))



print(logo)


points = 0

def next_questions(first, second):
    print('Compare A: ' + data[first]['name'],data[first]['description'],data[first]['country']  )
    print(data[first]['follower_count'])
    print(vs)

    print('Against B: ' + data[second]['name'],data[second]['description'],data[second]['country']  )
    print(data[second]['follower_count'])



game_finished = False
while not game_finished == True:
    random1 = random.randint(1,50-1)
    random2 = random.randint(1,50-1)
    next_questions(random1,random2)

    answer = input('Who has more followers Type "A" or "B "').lower()
    if answer == 'a':
        if data[random1]['follower_count'] >= data[random2]['follower_count']:
            print('You are wright')
            points += 1
        elif data[random1]['follower_count'] < data[random2]['follower_count']:
            print('You are wrong')
            print(f'YOU FINISHED THE GAME WITH {points} points')
            game_finished = True
   

    if answer == 'b':
        if data[random1]['follower_count'] <= data[random2]['follower_count']:
            print('You are wright')
            points += 1
        elif data[random1]['follower_count'] > data[random2]['follower_count']:
            print('You are wrong')
            print(f'YOU FINISHED THE GAME WITH {points} points')
            game_finished = True


    

