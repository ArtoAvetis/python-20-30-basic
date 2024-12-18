# exe-7

# n = int(input('Enter n:  '))
# x = 1
# for i in range(0, n):
#     for j in range(0, 2 * n - 1):
#         if j < (2 * n - 1) // 2 - i or j > (2 * n - 1) // 2 + i:
#             print('   ', end='')
#         else:
#             if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
#                 print(f'{x:>3}', end='  ')
#                 x += 2
#     print()

# exe -8

# n = int(input('Enter n:  '))
# for i in range(1, n + 1):
#     x = n
#     for j in range(1, n + 1):
#         if j <= i:
#             print(x, end=' ')
#             x -= 1
#         else:
#             print('.', end=' ')
#     x += 1
#     for j in range(1, n + 1):
#         if i + j > n:
#             print(x, end=' ')
#             x += 1
#         else:
#             print('.', end=' ')
#     print()

# exe- 9
# text = 'ssbsbsssbbbsbsbssssssssbs'
# text_s = 's' * len(text)
# while text_s not in text:
#     text_s = text_s[:-1]
# print(text_s, len(text_s))

# exe - 10

# n = int(input('Enter number count:  '))
# max_sum = 0
# for i in range(n):
#     number = int(input('Enter number: '))
#     number = str(number)
#     summ = 0
#     for j in number:
#         summ += int(j)
#     if summ > max_sum:
#         max_sum = summ
# print(max_sum)





  