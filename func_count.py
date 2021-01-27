def equally_count_not_special(numbers, signs):
    
    i = 0
    iteration = len(signs)
    while i < iteration:
        one = numbers.pop(0)
        two = numbers.pop(0)
        sign = signs.pop(0)
        if sign == '+':
            equalle = one + two
        if sign == '-':
            equalle = one - two
        
        numbers.insert(0, equalle)
        i += 1
    return numbers

def priority_multiplay(numbers, index):
    one = numbers.pop(index)
    two = numbers.pop(index)
    result = one * two
    numbers.insert(index, result)
    return numbers

def priority_division(numbers, index):
    one = numbers.pop(index)
    two = numbers.pop(index)
    result = one / two
    numbers.insert(index, result)
    return numbers

def defining_func (numbers, signs):
    arr_delete = []
    for i in range(len(signs)):
        if signs[i] == '*':
            arr_delete.append(i)
            priority_multiplay(numbers, i)
    for i in arr_delete: # i это числа
        signs.pop(i)
    arr_delete.clear()

    for i in range(len(signs)):
        if signs[i] == '/':
            arr_delete.append(i)
            priority_division(numbers, i)
    for i in arr_delete:
        signs.pop(i)
    arr_delete.clear()

    equally_count_not_special(numbers, signs)
    result = numbers[0]
    return result




