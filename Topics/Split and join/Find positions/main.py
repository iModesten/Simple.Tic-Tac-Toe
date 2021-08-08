# put your python code here
sequence = input().split()
number = int(input())
position_of_x = [str(i) for i in range(len(sequence)) if int(sequence[i]) == number]
if len(position_of_x) == 0:
    print("not found")
else:
    print(' '.join(position_of_x))
