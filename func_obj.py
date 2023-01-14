def multiplier_by_two(n):
    return n * 2

def add_two(n):
    return n + 2

def applied_operation(f, numbers):
    outcomes = []
    for number in numbers:
        outcome = f(number)
        outcomes.append(outcome)

&gt;&gt;&gt; nums = [1, 2, 3]
&gt;&gt;&gt; applied_operation(multiplier_by_two, nums)
[2, 4, 6]

&gt;&gt;&gt; applied_operation(add_two, nums)
[3, 4, 5]