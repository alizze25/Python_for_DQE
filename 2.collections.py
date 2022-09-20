#
#
# # sequences, common workflow
# # indexing, index()
#
# a = ('a', 'b', 'a', 1, 2)
# print(a.index('a'))
# a = 'avc'
# # print(a[:-2])
#
# # len()
#
# # print(len(('a', 'b', 'c', 1, 2)))
#
# # for i in a:
# #     print(i)
#
#
# # count()
#
# #print(a.count('c'))
#
# # list
# # sort(), sorted()
#
# # a = [1, 3, 2]
# #
# # #a.sort()
# # #print(a)
# #
# # b = sorted(a)
# # #print(b)
# #
# # # append()
# #
# # a.append(8)
# # print(a)
# #
# # # insert()
# #
# # a.insert(1, 8)
# # print(a)
# #
# # # pop()
# #
# # b = a.pop(1)
# # print(b)
# #
# # # remove()
# #
# # a.remove(8)
# # print(a)
# # # reverse()
# # a.reverse()
# # print(a)
#
# a = [1, 3, 5, 2]
# b = a
#
# a.sort()
# print(a)
#
# # copy()
#
# b = a.copy()
# a.reverse()
#
# print(b)
#
# # clear()
#
# b.clear()
# print(b)

# mapping, dict

a = {'a': 1, 'b': 42, (1, 2, 3): 34, True: 99}
#print(a)
# # get()
#
# #print(a.get(True))
# print(a[True])
#
#
# # update()
# a[(1, 2, 3)] = 344
# print(a)
#
# # fromkeys()
#
# b = a.fromkeys([1,2,3], 0)
# print(b)


# keys(), values(), items()

# for key in a.keys():
#     if key == 'a':
#
#     print('value', value)


# setdefault()

a = {'city': 'Minsk',
     'country': 'BY',
     'year': 2021}

print(a)

#print(a.setdefault('month', 'N/A'))
#print(a['month'])

# sets, difference()

a = {1, 2, 3}
b = {3, 4, 5}
print(b.difference(a))

c = frozenset({7,8,9})
print(type(c))


# note: collections, OrderedDicts and Counter

from collections import OrderedDict, Counter
a = {'city': 'Minsk',
     'country': 'BY',
     'year': 2021}


print(Counter(a))