# list = [4, 9, 26, 10, 23, 67, 2]
# nor_list = []
# for i in list:
#     if i % 2 == 0:
#        nor_list.append(i)
# print(nor_list)

# list = [1, 5, -9, 100, 36, 9]
# for i in list:
#     if list.count (i) == 1:
#         print(i)
    

# exe - 1

# tuple = (4,5,6,9,8,52,6,6,6,9,4,5)
# print(list.count(5), end=' ')

# exe-2
   
# list = ['Avetisyan', 'Artavazd', 'Sureni']
# list.sort(reverse = True)
# print(list)

# exe-3 

# list = ['Avetisyan', 'Artavazd', 'Sureni']
# list.sort(key=len)
# print(list)

# exe-4

# list = ['es', 'sovorum em', 'smart codum']
# print(' '.join(list))

# exe-5

# list = [1, 12, 15]
# sum = sum(list)
# print(f'{list} ---- {sum}')

# exe-6

# anun = ['Artavazd', 'Armine', 'Artur', 'Meri']
# pntrvox_anun = input('mutqagreq anun:   ')
# if pntrvox_anun in anun:
#    print('gtnvel e')
# else:
#    print('chi gtnvel') 

# exe-3

# list = ['im', 'aghjike', 'ereq', 'tarekan e']
# erkar_text = max(list, key = len)
# print(erkar_text)

# exe-4

# list1 = ['arev', 125, -32, 'krak']
# list2 = ['krak', 'jur', 12, 74]
# for i in list2:
#     if i in list1:
#         print('chisht e')
#         break
# else:    
#      print('sxal e')   


# exe-1

# list = []
# list.append('text')
# list.append(4.25)
# list.append(52)
# list.append((1,2,3))
# list.append({'python programmer'})
# list.append({-1, -9,})
# print(list)

# exe-2

# list = ['Hp', 'Asus', 'Dell', 'Mac', 'Lenovo']
# if 'Mac' in list:
#     print(True)
# else:
#     print(False)    

# exe-3
# cackagir = input('mutqagreq dzer cackagiry:  ')
# for i in cackagir:
#     if len(cackagir) >= 8 and (i.isdigit() for i in cackagir) and (i.isalpha() for i in cackagir):
#        print(f'{cackagir} --- cackagiry vstaheli e')
#        break
# else:
#     print(f'{cackagir} --- cackagiry vstaheli che')   
    
# exe-4

# link = "https://www.youtube.com/watch?v=RRW2aUSw5vU"
# print(link[link.index('=') + 1:])
# link = link.split('=')
# print(link[1])


# exe-5

# text = input('mutqagreq text:  ').replace(' ', '')
# if text == text[::-1]:
#     print('bac e')
# else:
#     print('pak e')

# exe-6

# text = 'Avetisyan---Artavazd'
# text = list(text)
# print(text)
          
# exe-7

# numbers = input('Enter 5 numbers: ')
# print([int(i) for i in numbers.split(' ') if int(i) % 2 == 0])
        
# exe-8

# list = [4, 25, -1, 38, 7]
# for i in list:
#     if i % 2 != 0:
#         print(i, end=' ')  

# exe-9  

# import random
 # group1 = ['Armen', 'Sahak', 'Karine', 'Anna', 'David']
# group2 = ['Armen', 'Sahak', 'Karine', 'Anna', 'David']
# final_list = []
# while group1 != []:
#     u1 = random.choice(group1)
#     u2 = random.choice(group2)
#     if u1 == u2:
#         if len(group1) == 1 == len(group2):
#             group1 = ['Armen', 'Sahak', 'Karine', 'Anna', 'David']
#             group2 = ['Armen', 'Sahak', 'Karine', 'Anna', 'David']
#             final_list = []
#         else:
#             continue
#     else:
#         final_list.append(f'{u1} --> {u2}')
#         group1.remove(u1)
#         group2.remove(u2)
# for i in final_list:
#     print(i)       








