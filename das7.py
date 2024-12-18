# summ = 0
# count = 0
# while True:
#     tiv = input('mutqagreq tiv:   ')
#     if tiv == '':
#         break
#     else:
#         summ += int(tiv)
#         count +=1
# print(summ)

# print(summ//count)
       
# kassa = 0
# while True:
#     tariq = input('mutqagreq tariq:  ')
#     if tariq == '':
#         break
#     else: 
#         tariq = int(tariq)
#     if 2 >= tariq >= 0:
#            continue
#     elif 12 >= tariq > 2:
#         kassa += 14
#     elif 65 >= tariq >= 12:
#          kassa += 23
#     else:
#          kassa += 18
# print(kassa)


# text = input('mutqagreq text:  ')
# for i in (text):
#    print(chr(ord(i) + 3), end='')
   


# pi = 3
# a = 2
# b = 3
# c = 4
# for i in range(15):
#     pi += (4 / (a * b * c)) * ((-1) ** i)
#     a, b, c, = a + 2, b + 2, c + 2
# print(pi)

# import random
# count_o = 0
# count_p = 0
# s = ''
# while True:
#     if count_o == 3 or count_p == 3:
#         break
#     random_letter = random.choice("OP")
#     if random_letter == "O":
#         s += 'O'
#         count_o += 1
#         count_p = 0
#     else:
#         s += 'P'
#         count_p += 1
#         count_o = 0
# print(s)


# exe-1  

# sum = 0
# count = 0
# while True:
#     number = int(input('enter number:  '))
#     if number == 0:
#         break
#     else:
#         sum += number
#         count += 1
# print(sum / count)        

# exe-2

# for i in range(5, 26, 5):
#     number = i - 0.05
#     print(f'price = ${number} --- discount = $ {round(number * 60 / 100, 2)} --- final_price = $ {round(number - number * 60 / 100, 2)}')
 
# exe-3

# for i in range(0, 101, 10):
#     celsius = i
#     fahrenheit = celsius * 1.8 + 32
#     print(f'{i} (C) --- {fahrenheit} (F)')

# exe-4
# text = input('enter text:  ').replace(' ', '')
# print(text == text[::-1])

# exe-5

# text = input('enter text:  ')
# for i in text:
#      if i.isdigit():
#           continue
#      elif i.isalpha():
#           continue
#      else:
#           text == text.replace(i, '')
# print(text == text[::-1])   

# exe-6  
# code = input('enter code: ')
# code = code[::-1]
# number = 0
# for i in range(0,len(code)):
#     number += int(code[i]) * 2 ** i
# print(number)    

