lies = [5,3,0,2,6,2,0,7,2,5]
frontelimination = 2

def detector(statement):
    for num in statement:
        if num == 0:
            statement.remove(num)
    for answer in statement:
        if answer > len(statement):
            print(f'{answer} true')
        else:
            print(f'{answer} false')
    
    for answer in statement[:frontelimination]:
        answeridx = statement.index(answer)
        answer -= 1
        statement[answeridx] = answer
    
    statement = sorted(statement, reverse=True)
    print(statement)

detector(lies)