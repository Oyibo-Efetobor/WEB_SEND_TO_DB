letter_head = [' A', ' B', ' C']
row_1 = ['⬜','⬜','⬜']
row_2 = ['⬜','⬜','⬜']
row_3 = ['⬜','⬜','⬜']

map = [row_1,row_2,row_3]
print(f"{row_1}\n{row_2}\n{row_3}")

user_input = input('Where would you like to place the marker?: ') #a2

letter_dictionary = {
    'a':0,
    'b':1,
    'c':2
}





horizontal = int(user_input[1])

vertical = int(letter_dictionary[user_input[0].lower()])

row_update = map[horizontal]

row_update[vertical] = '❌'

print(letter_head)
print(f"{row_1}\n{row_2}\n{row_3}")
