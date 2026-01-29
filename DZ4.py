#DZ1
Задача 1

print(17/2*3+2)
print(2+17/2*3)
print(19%4+15/2*3)
print(15+6-10*4)
print(17/2%2*3**3)

Ответы 

27.5
27.5
25.5
-19
13.5

Задача 2

print(17/2*(3+2))
print(((2+17)/2)*3)
print((19%(4+15)/2)*3)
print((15+6-10)*4)
print((17/2)%(2*3**3))

Задача 3

days = int(input("Введите сутки: "))
print(f'{days * 24} час(-ов) {days * 1440} минут(-ы) {days * 86400} секунд(-ы)')

Вывод

Введите сутки: 5
120 час(-ов) 7200 минут(-ы) 432000 секунд(-ы)

Задача 4

days = 182  
weeks = days // 7  
print(weeks) 

Вывод

26

Задача 5

side_1 , side_2  = map(int, input().split())
print(side_1  // 30 * (side_2  // 30))

Вывод

150 65
10

#DZ2
Задача 1

print(int(input())%10 == 3)

Задача 2

input_string = input("введите три числа через пробел: ")
numbers = input_string.split()
A = int(numbers[0])
B = int(numbers[1])
C = int(numbers[2])
proga = A < 0 or B < 0 or C < 0
print(proga)

Задача 3

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
if (num1 + num2) % 2 == 1:
    print("Числа разной четности")
elif num1 % 2 == 0 and num2 % 2 == 0:
    print("Числа четные")
else:
    print("Числа нечетные")

Задача 4

a = int(input("Введите двухзначное число:"))
b = (a%100//10)+(a%10)
n = 0
 
if b > 9:
    print("Сумма цифр числа является двузначной.")
 
else:
    while True:
        n += 1
        a += 1
        b = (a%100//10)+(a%10)
        if b > 9:
            print("Сумма цифр числа не является двузначной.")
            print(f"Ближайшее число, удовлетворяющее условию, встретиться через {n} чисел. Число - {a}.")
            break
    

Задача 5

n = input()
n1 = n[0]
n2 = n[1]
n3 = n[2]
n4 = n[3]
if n1 == n2 or n1 == n3 or n1 == n4 or n2 == n3 or n2 == n4 or n3 == n4:
    print("YES")
else:
    print("NO")

Задача 6

s = input() 
print(s[2]) 
print(s[-2]) 
print(s[:5]) 
print(s[:-2]) 
print(s[ : : 2]) 
print(s[1 : : 2]) 
print(s[ : : -1]) 
print(s[ : : -2]) 
print(len(s))

Задача 7

s = input()
s[0] == s[-1] and not print('yes', s[0]) or print('no')

Задача 8

string = input('Введите слово: ')
string_reversed = reversed(string)
if "yes" == "".join(set(["yes" if i == j else "no" for i, j in zip(string, string_reversed)])):
    print("yes")
else:
    print("no")


Задача 9

s = input()
count = len(s) - len(s.replace('f', ''))
if count == 0:
    pass
elif count == 1:
    print(s.index('f'))
else: 
    print(s.index('f'), count)

Задача 10

k = int(input())
l = int(input())
m = int(input())
n = int(input()) 

print("YES" if not ((k + l + m + n) % 2) else "NO")

#DZ3
Задача 1

n = int(input())
for i in range(1, n):
    print(i)

Задача 2

for _ in range(20):
    print(10)

Задача 3

i, n, res = 0, int(input()), 0 
while i != n+1:  # n включительно
    if i % 2 == 0:
        res += i 
    i += 1 
print(res) 

Задача 4

n = input("Введите натуральное число: ")
product = 1
found = False
for d in n:
    if d != '0' and int(d) % 2 == 0:
        product *= int(d)
        found = True
if found:
    print("Произведение цифр:", product)
else:
    print("Нет подходящих цифр.")

Задача 5

n = int(input("Введите натуральное число: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")

Задача 6

n = int(input("Введите число n: "))
i = 1
while i * i < n:
    print(i * i, end=" ")
    i += 1
    
#DZ4

# 1. 
n = int(input())
for i in range(1, n + 1):
    print(i)

# 2. 
for _ in range(20):
    print(10)

# 3. 
n = int(input())
total = 0
for i in range(0, n + 1):
    if i % 2 == 0:
        total += i
print(total)

# 4. 
num = int(input())
product = 1
has_even_digit = False
for digit in str(num):
    d = int(digit)
    if d != 0 and d % 2 == 0:
        product *= d
        has_even_digit = True
if has_even_digit:
    print(product)
else:
    print(1)  

# 5. 
n = int(input())
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)

# 6. 
n = int(input())
i = 1
while i * i < n:
    print(i * i)
    i += 1

# 7. 
num = input()
sum_digits = sum(int(d) for d in num)
print(sum_digits)

# 8. 
num = input()
min_digit = min(int(d) for d in num)
print(min_digit)

# 9. 
text = input()
import re
text = re.sub(r'\s+', ' ', text)
text = re.sub(r',\s*', ', ', text)
print(text)

# 10. 
n = int(input())
for i in range(1, n + 1):
    if 11 <= i % 100 <= 14:
        form = 'коров'
    else:
        last_digit = i % 10
        if last_digit == 1:
            form = 'корова'
        elif 2 <= last_digit <= 4:
            form = 'коровы'
        else:
            form = 'коров'
    print(f"На лугу {i} {form}")
   
#DZ5
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

#dictionary = {}
#while True:
#    line = input().strip()
#    if line.endswith('.'):
#        break
#    term, definition = line.split(' – ', 1)
#    dictionary[term.strip()] = definition.strip()
#m = int(input().strip())
#for _ in range(m):
#    query = input().strip()
#    if query in dictionary:
#        print(dictionary[query])
#    else:
#        print("Не найдено")

#DZ6
# 1. 
try:
    x = (1, 2, 5, 7)
    x = x / 2  
    print(x)
except Exception as e:
    print(f"Ошибка: {type(e).__name__}: {e}")

# 2. 
try:
    lst = [1, 2, 3]
    index = int(input("Введите индекс: "))
    print(lst[index])
except IndexError as e:
    print("IndexError: попытка обращения к несуществующему элементу списка.")

# 3. 
try:
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))
    if a == 0 or b == 0 or c == 0:
        raise ArithmeticError("Длина стороны не может быть равна 0.")
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f"Площадь треугольника: {area}")
except ArithmeticError as e:
    print(f"ArithmeticError: {e}")

# 4. 
try:
    lst = [1, 2, 3]
    elem = int(input("Введите элемент для удаления: "))
    lst.remove(elem)
    print(f"Обновленный список: {lst}")
except ValueError:
    print("ValueError: попытка удалить элемент, которого нет в списке.")
except TypeError:
    print("TypeError: введены некорректные данные.")

# 5. 
try:
    my_dict = {'a': 1, 'b': 2}
    key = input("Введите ключ: ")
    value = my_dict[key]
    print(f"Значение: {value}")
except KeyError:
    print("KeyError: такого ключа нет в словаре.")

# 6. 
try:
    line = input("Введите числа, разделённые пробелами: ")
    total = 0
    for part in line.split():
        try:
            num = int(part)
            total += num
        except ValueError:
            continue
    print(f"Сумма: {total}")
except Exception as e:
    print(f"Произошла ошибка: {e}")

# 7. 
try:
    s = input("Введите строку: ")
    if not isinstance(s, str):
        raise TypeError("Входные данные не строка.")
    freq = {}
    for ch in s:
        if ch.isalpha():
            freq[ch] = freq.get(ch, 0) + 1
    for ch, count in freq.items():
        print(f"{ch} {count}")
except TypeError:
    print("TypeError")
    
#DZ7
# 1. 
def m(a, b):
    return a if a < b else b

# 2. 
def is_perfect(n):
    if n <= 1:
        return False
    sum_divisors = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors == n

# 3. 
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 4. 
def closest_mod_5(x):
    remainder = x % 5
    if remainder == 0:
        return x
    else:
        return x + (5 - remainder)

# 5. 
def check_variable(v):
    if v == "Поработали, и хватит":
        return None
    if not v:
        return "Нельзя использовать"
    if not (v[0].isalpha() or v[0] == '_'):
        return "Нельзя использовать"
    for ch in v:
        if not (ch.isalnum() or ch == '_'):
            return "Нельзя использовать"
    return "Можно использовать"

# 6. 
odd_two_digit_numbers = [i for i in range(10, 100) if i % 2 == 1]

# 7. 
three_digit_multiples = [i for i in range(100, 1000) if i % 3 == 0 and i % 5 == 0]

# 8. 
def count_unique(lst):
    count = 0
    for i in range(len(lst)):
        is_unique = True
        for j in range(i):
            if lst[i] == lst[j]:
                is_unique = False
                break
        if is_unique:
            count += 1
    return count

# 9. 
def neighbor_sums(lst):
    n = len(lst)
    if n == 1:
        return lst
    result = []
    for i in range(n):
        left = lst[i - 1]
        right = lst[(i + 1) % n]
        result.append(left + right)
    return result

#DZ8
# 1. 
def log_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Результат: {result}')
        return result
    return wrapper

@log_result
def square(x):
    return x ** 2

# 2. 
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f'Hello, {name}')

# 3. 
def bench(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'Ошибка: {type(e).__name__}, сообщение: {e}')
    return wrapper

@bench
def faulty_division(x, y):
    return x / y

# 4. 
words = ['apple', 'banana', 'cherry']
lengths = [len(word) for word in words]

# 5. 
words_list = ['apple', 'Banana', 'cherry', 'DATE']
lowercase_words = [word for word in words_list if word.islower()]

# 6. 
people = [('Ivan', 20), ('Anna', 17), ('Peter', 25)]
adults = [person for person in people if person[1] > 18]

# 7. 
from functools import reduce
list_of_lists = [[1, 2], [3, 4], [5, 6]]
flat_list = reduce(lambda acc, x: acc + x, list_of_lists, [])

# 8. 
words_set = ['cat', 'car', 'mouse', 'dog', 'snake', 'cow']
from collections import defaultdict
dict_by_letter = defaultdict(list)
for word in words_set:
    dict_by_letter[word[0]] += [word]
# Или через обычный словарь
dict_by_letter = {}
for word in words_set:
    key = word[0]
    if key not in dict_by_letter:
        dict_by_letter[key] = []
    dict_by_letter[key].append(word)

# 9. 
items = [('apple', 2, 5), ('banana', 1, 10), ('cherry', 3, 4)]
sums = [price * quantity for _, price, quantity in items]            