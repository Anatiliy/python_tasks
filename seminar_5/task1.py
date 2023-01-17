# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более
# чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота

# b) Подумайте как наделить бота 'интеллектом'


import random

def game(gamer, numbers_of_candies):
    print(f'осталось {numbers_of_candies} конфет')
    my_candy = int(input(f'{gamer}, сколько конфет забираете? '))
    if numbers_of_candies < my_candy:
        print('столько конфет нет')
        return game(gamer, numbers_of_candies)
    elif 28 < my_candy:
        print('столько конфет брать нельзя')
        return game(gamer, numbers_of_candies)
    numbers_of_candies -= my_candy
    return numbers_of_candies


def gamer_bot(numbers_of_candies):
    print(f'осталось {numbers_of_candies} конфет')
    if numbers_of_candies < 29:
        print(f'бот забрал {numbers_of_candies} конфет')
        return 0
    elif 28 < numbers_of_candies < 57:
        print(f'бот забрал {numbers_of_candies - 29} конфет')
        return 29
    else:
        bot_candies = random.randint(1, 28)
        print(f'бот забрал {bot_candies} конфет')
        return numbers_of_candies - bot_candies




if input('если хотите играть с ботом, введите "b", если хотите играть с живым игроком, нажмите enter ') == 'b':
    
    name_of_gamer = input('введите своё имя ')
    numbers_of_candies = int(input('сколько конфет положить в вазу '))
    while numbers_of_candies:
        numbers_of_candies = game(name_of_gamer, numbers_of_candies)
        if not numbers_of_candies:
            print(name_of_gamer,'победил!!!')
            break
        numbers_of_candies = gamer_bot(numbers_of_candies)
        if not numbers_of_candies:
            print('bot победил!!!')
            break

else:
    
    name_of_gamers = input('введите имена игроков через пробел ').split()
    numbers_of_candies = int(input('сколько конфет положить в вазу '))
    while numbers_of_candies > 0:
        for gamer in name_of_gamers:
            numbers_of_candies = game(gamer, numbers_of_candies)
            if not numbers_of_candies:
                print(gamer,'победил!!!')
                break
    

