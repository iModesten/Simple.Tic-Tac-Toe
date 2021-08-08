height = int(input())
triangle_list = []
for i in range(height):
    if len(triangle_list) == 0:
        triangle_list.append('#')
    else:
        triangle_list.append((len(triangle_list[i - 1]) * '#' + '#' * 2))
triangle_list_updated = [el.center(len(triangle_list[-1])) for el in triangle_list]
print('\n'.join(triangle_list_updated))

