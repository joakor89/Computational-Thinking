
def split_list_items(roster, divider):
    try:
        return [i / divider for i in roster]
    except ZeroDivisionError as e:
        print(e)
        return roster

roster = list(range(10))
divider = 4

print(split_list_items(roster, divider))

