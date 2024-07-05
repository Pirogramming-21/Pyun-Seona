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

def brGame():
    num = 0
    while num < 31:
        num = player_turn("Player A", num)
        if num >= 31:
            print("playerB win!")
            break
        num = player_turn("Player B", num)
        if num >= 31:
            print("playerA win!")
            break

brGame()