
import re
l2 = list()
input_txt = ''
while True:
    input_txt = input('>> ')
    if input_txt == '=':
        break
    else:

        if re.fullmatch(r'(-?\d+(\.\d+)?)|([-+*:])', input_txt):
            l2.append(input_txt)
            print('{} ...'.format(''.join(l2)))

#
# TODO if int or float
result = ''
try:
    result = int(l2[0])
except ValueError:
    pass
try:
    result = float(l2[0])
except ValueError:
    pass

mark = ''
for i in l2[1:]:
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
