import random

num = 0

def get_input():
    while True:
        try:
            input_num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
            if 1 <= input_num <= 3:
                return input_num
            else:
                print("1,2,3 중 하나를 입력하세요")
        except ValueError:
            print("정수를 입력하세요")
            
def player_turn(player_name, current_num):
    count = get_input()
    for i in range(1, count + 1):
        current_num += 1
        print(f"{player_name} : {current_num}")
    return current_num

#컴퓨터 차례(9단계)
def computer_turn(current_num):
    count = random.randint(1,3)
    for i in range(1, count+1):
        current_num += 1
        print(f"computer: {current_num}")
        if current_num >= 31:
            return current_num
    return current_num

def brGame():
    num = 0
    while num < 31:
        num = computer_turn(num)
        if num >= 31:
            print("Player wins!")
            break
        num = player_turn("Player", num)
        if num >= 31:
            print("computer win!")
            break
brGame()