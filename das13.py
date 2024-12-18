# mydict = {'a':1,'b':2,'c':12}
# x = 1
# for i in mydict:
#     x *= mydict[i]
# print(x)
# ---------------------------------------------------

# mydict = {'a':1,'b':2,'c':12}
# for i in mydict:
#     print(mydict[i])
# ---------------------------------------------------

# dict_ = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# keys = sorted(dict_)
# print(keys)
# values = sorted(dict_.values())
# print(values)
# ---------------------------------------------------


# dict_ = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# keys = sorted(dict_, key=dict_.get, reverse=True)[:3]
# newdict = {}
# for i in keys:
#     newdict[i] = dict_[i]
# print(newdict)
# ---------------------------------------------------

# dict_ = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# print({i:dict_[i] for i in sorted(dict_, key=dict_.get, reverse=True)[:3]})
# ---------------------------------------------------


# students = {
#     "Arman":7,
#     "Karen":4,
#     "Hakob":10,
#     "Vardan":5,
#     "Sergo":6,
#     "Gor":8
# }
# good = []
# bad = []
# good = {}
# bad = {}
# summ = 0
# for i in students:
#     summ += students[i]
# mean = round(summ / len(students), 2)
# for i in students:
#     if students[i] >= mean:
#         good[i] = students[i]
#     else:
#         bad[i] = students[i]
# print(good)
# print(bad)
# ---------------------------------------------------
# phone = {
#     '1':'.,?!:',
#     '2':'ABC',
#     '3':'DEF',
#     '4':'GHI',
#     '5':'JKL',
#     '6':'MNO',
#     '7':'PQRS',
#     '8':'TUV',
#     '9':'WXYZ',
#     '0':' '
# }
# text = input('Enter text: ').upper()
# for i in text:
#     for j in phone:
#         if i in phone[j]:
#             print(j * (phone[j].index(i) + 1), end='')
# ---------------------------------------------------
# dict_ = {
#     1 :'AEILNORSTU',
#     2 :'DG',
#     3 :'BCMP',
#     4 :'FHVWY',
#     5 :'K',
#     8 :'JX',
#     10:'QZ',
# }
# name = input('Enter name: ').upper()
# summ = 0
# for i in name:
#     for j in dict_:
#         if i in dict_[j]:
#             summ += j
# print(summ)
# ---------------------------------------------------



# exe-7

          

# exe-8

# dict = {}
# text = 'exercies'
# for i in text:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
# print(dict)            


