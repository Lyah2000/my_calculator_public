from tkinter import messagebox

def check_point_and_separation_sign(arr):
    
    signal = 0
    for i in range(len(arr)):
        if arr[i] == ".":
            index_point = i
            lenght_sign = len(arr)
            signal = 1
    
    if signal == 0:
        number = from_not_point(arr) 
        return number
    if signal == 1:
        whole_part, fractional_part = from_point(arr, index_point, lenght_sign) # тип str и это строки
        number_whole = from_not_point(whole_part)
        number_fractional = from_point_fractional(fractional_part)
        number = number_whole + number_fractional
        return number

def from_point(arr_from_point, index_point, lenght_sign):
    before_point = []
    later_point = []

    i = 0
    while i < index_point:
        before_point.append(arr_from_point[i])
        i += 1
    index_point += 1
    while index_point < lenght_sign:
        later_point.append(arr_from_point[index_point])
        index_point += 1

    return before_point, later_point

def from_point_fractional(arr_fractional):
    number = 0
    lenght = len(arr_fractional)
    i = 0
    power = 1
    while i < lenght:
        number += arr_fractional[i] * 10 **((-1)*power)
        power += 1
        i += 1
    return number


def from_not_point(arr_from_not_point):
    
    lenght = len(arr_from_not_point)
    number = 0
    i = 0
    while i < len(arr_from_not_point):
        
        number += arr_from_not_point[i] * (10 ** (lenght-1))
        lenght -= 1
        i += 1
        
    return number

def of_string_in_float(line): # после данной функции массив будет иметь все числа типом инт, не считая точки, точка останется строковой
    arr = []    
    for i in line:
        if i == "0":
            arr.append(0)
        elif i == "1":
            arr.append(1)
        elif i == "2":
            arr.append(2)
        elif i == "3":
            arr.append(3)    
        elif i == "4":
            arr.append(4)
        elif i == "5":
            arr.append(5)
        elif i == "6":
            arr.append(6)
        elif i == "7":
            arr.append(7)
        elif i == "8":
            arr.append(8)
        elif i == "9":
            arr.append(9)
        elif i == ".":
            arr.append(".")
        else:
            messagebox.showerror("Сообщение для дебилов", "Ну и как ты собираешься складывать буквы???")
   
    return arr 
