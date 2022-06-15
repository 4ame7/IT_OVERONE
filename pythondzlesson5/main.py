import random

while True:
    print('Вы играете в камень ножницы бумага. к - камень, н - ножницы, б - бумага. Чтобы выйти  напишите: выход.')
    player = input('Вы выбрали:')
    if player not in ['к', 'н', 'б', 'выход']:
        print('Не правильный ввод!')

    if player == 'выход':
        break;

gen = {1:'к', 2:'н', 3:'б'}
comp_choice = gen[random.randint(1, 3)]
print(f'Бот выбрал: {comp_choice}')
win_combination = [('к','н'),('н','б'),('б','к')]
if player == comp_choice:
    print('Ничья')
elif (player,comp_choice) in win_combination:
    print('Игрок победил')
else:
    print('Победа бота')