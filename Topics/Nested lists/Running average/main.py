string_digits = list(input())
list_digits = [int(i) for i in string_digits]
result_list = [(list_digits[i] + list_digits[i + 1]) / 2 for i in range(0, len(list_digits) - 1)]
print(result_list)
