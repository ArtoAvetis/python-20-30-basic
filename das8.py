# for i in 'abc':
#     for j in range(1, 4):
#         print(i,j, end=' ')
#     print()    

# for i in range(1 , 11):
#     for j in range(1, 11):
#         print(f'{i * j:>5}', end= '')
#     print()    

# exe-4

# n = 6
# for i in range(n + 1):
#     for j in range(n + 1):
#         if i == j or n == i + j:
#           print('^', end='')
#         else:
#          print(' ', end='')
#     print()

# exe-2

# tiv = int(input('mutqagrqe tiv: '))
# for i in range(1, tiv + 1):
#     for j in range(i):
#         print(i, end=' ')
#     print()    

# exe-1

# for i in range(0, 6):
#     for j in range(i, 11 + i, 2):
#         print(f'{j:>3}', end=' ')
#     print()             

# exe-3

# n = int(input('mutqagreq tiv:  '))
# for i in range(0, n + 1):
#     for j in range(0, n + 1):
#         if j == 0 or j == n:
#            print('|',end='')
#         elif i == 0 or i == n:
#              print('--',end='')
#         else:
#             print('  ',end='')     
#     print()           

# exe-5

# qanak = 0
# n = int(input('mutqagreq tveri qanak:  '))
# for i in range(0, n):
#     tiv = int(input('mutqagreq tiv:  '))
#     for i in range(2, tiv):
#         if tiv % i  == 0:
#          break
# else:
#     qanak += 1
# print(qanak)

# exe-8

# n = int(input('mutqagreq tiv:  '))
# for i in range(n):
#     probel = ' ' * (n - i - 1)
#     hashtag = '#' * ( 2 * i + 1)
#     print(probel + hashtag)

# n = int(input('mutqagreq tiv:  '))
# for i in range(n):
#     for j in range(2 * n - 1):
#         if j < (2 * n - 1) // 2 - i or j > (2 * n - 1 ) // 2 + i:
#             print(' ', end=' ')
#         else:
#             print('#', end=' ') 
#     print() 
   
# exe-6

# n = int(input('mutqagreq tiv:'  ))
# qanak = 0
# for i in range(1, n + 1):
#     factorial = 1
#     for j in range(1, i + 1):
#         factorial *= j
#     qanak += factorial
# print(qanak)   
    
           