# write your code here
def main_function():
    # lines = list(input("Enter cells: "))
    # game_grid = [lines[symbol:symbol + 3] for symbol in range(0, len(lines), 3)]
    game_grid = [[' ', ' ', ' '] for symbol in range(3)]
    create_grid(game_grid)
    make_move(game_grid)


def create_grid(game_grid):
    first_line = ' '.join(game_grid[0][0:3])
    second_line = ' '.join(game_grid[1][0:3])
    third_line = ' '.join(game_grid[2][0:3])
    print(f"""---------
| {first_line} |
| {second_line} |
| {third_line} |
---------""")


def make_move(game_grid):
    last_symbol = ' '
    while True:
        coordinates = input("Enter the coordinates: ").split()
        if coordinates[0] not in '0123456789' or coordinates[1] not in '0123456789':
            print("You should enter numbers!")
            continue
        elif int(coordinates[0]) < 1 or int(coordinates[0]) > 3 or int(coordinates[1]) < 1 or int(coordinates[1]) > 3:
            print("Coordinates should be from 1 to 3!")
            continue
        elif game_grid[int(coordinates[0]) - 1][int(coordinates[1]) - 1] is not ' ':
            print("This cell is occupied! Choose another one!")
            continue
        else:
            if last_symbol == ' ' or last_symbol == 'O':
                game_grid[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = 'X'
                last_symbol = 'X'
                create_grid(game_grid)
            else:
                game_grid[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = 'O'
                last_symbol = 'O'
                create_grid(game_grid)
        if game_result(game_grid):
            break


def game_result(game_grid):
    list_lines = game_grid + [[column[j] for column in game_grid] for j in range(3)]
    list_lines.append(list(game_grid[0][2] + game_grid[1][1] + game_grid[2][0]))
    list_lines.append(list(game_grid[0][0] + game_grid[1][1] + game_grid[2][2]))
    count_x = 0
    count_o = 0
    for i in game_grid:
        for j in i:
            if j == 'X':
                count_x += 1
            elif j == 'O':
                count_o += 1
    # if abs(count_x - count_o) >= 2:
    #     print("Impossible")
    # elif ['X', 'X', 'X'] in list_lines and ['O', 'O', 'O'] in list_lines:
    #     print("Impossible")
    if ['X', 'X', 'X'] in list_lines:
        print("X wins")
        return "X wins"
    elif ['O', 'O', 'O'] in list_lines:
        print("O wins")
        return "O wins"
    elif ' ' not in [i for line in list_lines for i in line]:
        # [[line[i] for i in range(len(line))] for line in list_lines]:
        print("Draw")
        return "Draw"
    # elif all(all([line[i] for i in range(len(line))]) for line in list_lines):
    #     print("Draw")
    #     return "Draw"
    # elif '' in [symbol for row in list_lines for symbol in row]:
    #     print("Game not finished")
    # else:
    #     print("Draw")


main_function()
