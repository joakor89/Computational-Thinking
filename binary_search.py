

objetive = int(input('Please! choose a number: '))
epsilon = 0.001
low = 0.0
high = max(1.0, objetive)
answer = (high + low) / 2


while abs(answer**2 - objetive) >= epsilon:
    print(f'Low {low}, High {high}, Answer {answer}')
    if answer**2 < objetive:
        low = answer
    else:
        high = answer

    answer = (high + low) / 2


print(f'The root sqaure of {objetive} is {answer}')