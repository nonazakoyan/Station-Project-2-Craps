from random import choice

def foo(win_num, lose_num, SumOfDice, goal_numbers):
    if SumOfDice in win_num:
        return 1
    elif SumOfDice in lose_num:
        return 0
    elif SumOfDice in goal_numbers:
        print(f"Now your goal number is {SumOfDice}:")
        return SumOfDice
    if goal_numbers == []:
        return win_num[0]


arr = list(range(1, 7))
win_num = [7, 11]
lose_num = [2, 3, 12]
goal_numbers = [4, 5, 6, 8, 9, 10]
while True:
    dice1 = choice(arr)
    dice2 = choice(arr)
    SumOfDice = dice1 + dice2
    print(f"The sum of dice is {dice1} + {dice2} = {SumOfDice}")
    res = foo(win_num, lose_num, SumOfDice, goal_numbers)
    if res == 1:
        print("You won!!!")
        break
    elif res == 0:
        print("You Lose")
        break
    else: 
        win_num = [res]
        lose_num = [7]
        goal_numbers = []
