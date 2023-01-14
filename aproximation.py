# Solution Approach

# User required number
objetive = int(input('Please! choose a number: '))
# How close it would like to be to the answer
epsilon = 0.01
# How close each iteration get to the answer
close = epsilon**2
# It will get the answer on each iteration
answer = 0.0


while abs(answer**2 - objetive) >= epsilon and answer <= objetive:
    print(answer)
    answer += close 


if abs(answer**2 - objetive) >= epsilon:
    print(f'The root square it could not be found {objetive}')
else:
    print(f'The root square of {objetive} is {answer}')