lies = [5, 3, 0, 2, 6, 2, 0, 7, 2, 5]


def detector(statement):
    holdanswer = ''
    statement = sorted(statement)
    for answer in statement:
        if answer == 0:
            statement.remove(answer)
    if statement is False:
        return True
    for answer in statement:
        holdanswer = statement.pop(statement.index(answer))
        break
    for answer in statement:
        if holdanswer > len(statement):
            return False
        else:
            break
    statement = sorted(statement, reverse=True)
    for answer in statement[:holdanswer]:
        answer -= 1

    statement = sorted(statement, reverse=True)
    print(statement)
    detector(statement)


print(detector(lies))
