# Задача 1

#my_tuple = (5, 2, 9, 1, 7)
#max_element = max(my_tuple)
#min_element = min(my_tuple)
#difference = max_element - min_element
#print("Разность между максимальным и минимальным элементом:", difference)

#Задача 2

#tuple_data = (5, 2, -2, 7, -8, -9, 1)
#sign_changes = 0
#for i in range(1, len(tuple_data)):
    #if (tuple_data[i-1] > 0 and tuple_data[i] < 0) or (tuple_data[i-1] < 0 and tuple_data[i] > 0):
        #sign_changes += 1
#print("Количество изменений знака в кортеже:", sign_changes)

#Задача 3

#def is_prime(n):
#    if n <= 1:
#        return False
#    for i in range(2, int(n**0.5) + 1):
#        if n % i == 0:
#            return False
#    return True
#numbers_tuple = (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
#primes = [num for num in numbers_tuple if is_prime(num)]
#print("Простые числа в кортеже:", primes)

#Задача 4

#def find_min_not_in_second_list(list1, list2):
#    set_list2 = set(list2) 
#    not_in_list2 = [x for x in list1 if x not in set_list2]  
#    if not not_in_list2: 
#        return "нет такого элемента"
#    else:
#        return min(not_in_list2) 
#list1 = [4, 1, 6, 9]
#list2 = [8, 1, 2, 4, 9, 5, 7, 6]
#result = find_min_not_in_second_list(list1, list2)
#print(result)

#Задача 5

#def reverse_number(num):
#    return int(str(num)[::-1])
#numbers = [12, 13, 14, 19, 16, 23]
#result = []
#for num in numbers:
#    result.append(num)  
#    if num % 2 == 0:    
#        result.append(reverse_number(num)) 
#print(result)

#Задача 6

#elements = [4, 1, 5, 2, 2, 2, 4, 2]
#count_dict = {}
#for element in elements:
#    if element in count_dict:
#        count_dict[element] += 1
#    else:
#        count_dict[element] = 1
#for key, value in count_dict.items():
#    print(f'Элемент {key} встречается {value} раз(а).')

#Задача 7

#input_string = input("Введите последовательность чисел через пробел: ")
#umbers = input_string.split()
#seen_numbers = set()
#results = []
#for number in numbers:
#    if number in seen_numbers:
#        results.append("YES")
#    else:
#        results.append("NO")
#        seen_numbers.add(number)
#for result in results:
#    print(result)

#Задача 8


#Задача 9

#school = {'9а': 22,'9б': 23,'9в': 24,'9г': 26,'9д': 23,}
#school['9б'] = 27 
#school['9е'] = 26
#del school['9д']
#total_students = sum(school.values())
#print("Количество учащихся в классах:", school)
#print("Общее количество учащихся в 9 классах:", total_students)

#Задача 10

dictionary = {}
while True:
    line = input().strip()
    if line.endswith('.'):
        break
    term, definition = line.split(' – ', 1)
    dictionary[term.strip()] = definition.strip()
m = int(input().strip())
for _ in range(m):
    query = input().strip()
    if query in dictionary:
        print(dictionary[query])
    else:
        print("Не найдено")
