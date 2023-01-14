# Exhaustive enumeration

objetive = int(input('Choose an integer: '))
answer = 0

while answer**2 < objetive:
    print(answer)
    answer += 1

if answer**2 == objetive:
    print(f'The root square of {objetive} is {answer}')
else:
    print(f'The {objetive} does not have exact root square')