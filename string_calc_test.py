#l = ['1', '-', '2', '+', '5', '*', '10', ':', '0', '+', '1']
import re
# (-?\d+(\.\d+)?)|([-+*:])

mark = ''
l2 = list()
input_txt = ''
reg_check = re.compile(r'(-?\d+(\.\d+)?)|([-+*:])')

while True:
    input_txt = input('')
    if input_txt == '=':
        break
    else:
        # TODO check is num and mark
        if reg_check.fullmatch(input_txt):
            l2.append(input_txt)
            print('{} ...'.format(''.join(l2)))

result = int(l2[0])
for i in l2[1:]:
    #n = 0
    if i in ['+', '-', '*', ':']:
        mark = i
        continue
    #####
    try:
        i = int(i)
    except ValueError:
        pass
    try:
        i = float(i)
    except ValueError:
        pass
    if mark == '+':
        result += i
    elif mark == '-':
        result -= i
    elif mark == '*':
        result *= i
    elif mark == ':':
        try:
            result /= i
        except ZeroDivisionError as ze:
            print('Error: {}'.format(ze))
            result = None
            break
print(result)
