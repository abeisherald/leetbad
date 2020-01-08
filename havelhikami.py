lies = [5,3,0,2,6,2,0,7,2,5]
frontelimination = 2

def detector(statement):
    statement = sorted(statement, reverse=True)
    for answer in statement:
        if answer == 0:
            statement.remove(answer)
    if statement is False:
        return True
    statement = statement.remove(answer)
    for answer in statement:
        if answer > len(statement):
            return False
        else:
            return True
    statement = sorted(statement, reverse=True)
    for answer in statement[:frontelimination]:
        answeridx = statement.index(answer)
        answer -= 1
        statement[answeridx] = answer
    
    statement = sorted(statement, reverse=True)
    print(statement)

detector(lies)