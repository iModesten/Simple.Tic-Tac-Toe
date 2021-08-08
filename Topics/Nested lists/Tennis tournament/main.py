number_of_lines = int(input())
final_list = []
while number_of_lines > 0:
    player = input()
    player_list = player.split()
    final_list.append(player_list)
    number_of_lines -= 1
names_of_winners = [i[0] for i in final_list if i[1] == 'win']
print(names_of_winners)
print(len(names_of_winners))
