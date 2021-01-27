def append_number_if_not_empty(list, string):
  if (len(string)) > 0:
    list.append(float(string))
# list список, string строка

def parse_string(string):
  operands = []
  operators = []

  # Переменная хранящая текущий номер между знаками
  operand = str()

  for c in string:
    # Если нашли оператор, то добавить целое число в список
    # операндов и оператор в список операторов
    if c in "+-*/":
      append_number_if_not_empty(operands, operand)
      operand = str()
      operators.append(c)
    # Добавить цифру к операнду
    else: 
      operand += str(c)

  # Добавить последний операнд если строка заканчивается числом
  append_number_if_not_empty(operands, operand)

  return operands, operators


# operands, operators = parse_string('5+84*89-54+545*52')

# print(operands)
# print(operators)