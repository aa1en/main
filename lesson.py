my_list = []
while True:
    num = input('Enter number: ')
    if num == '':
        break
    else:
        my_list.append(int(num))
print(my_list)
finish = int(input('Enter finish number: '))
for i in my_list:
    for j in my_list:
        if i + j == finish:
            print(f'{finish} = ({my_list.index(i)},{my_list.index(j)})')
            break
        else:
            continue
    break
# Finish