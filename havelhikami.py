lies = [5, 3, 0, 2, 6, 2, 0, 7, 2, 5]


def detector(statement):
    while 0 in statement:
        statement.remove(0)
    if statement is False:
        return True
    statement = sorted(statement, reverse=True)
    holdanswer = statement.pop(0)
    if holdanswer > len(statement):
        return False
    for answer_idx in range(holdanswer):
        statement[answer_idx] -= 1
    detector(statement)


print(detector(lies))
