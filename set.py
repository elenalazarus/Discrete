def union(set1, set2):
    '''
    (list, list) -> (set)
    The function takes two sets, unites them into one and returns united set.
    >>> union([5, 2, 8, 12, 3, 7, 10, 23], [6, 23, 56, 3, 1, 3, 9, 0])
    {0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 23, 56}
    >>> union ([2, 5, 1, 11, 91, 32, 9, 45], [9, 2, 1, 5, 3, 7, 8])
    {32, 1, 2, 3, 5, 7, 8, 9, 11, 45, 91}
    '''
    un_state = set1 + set2
    return set(un_state)


def not_set(set1, set2, numb):
    '''
    (list, list, str) -> (set)
    This function takes two lists of numbers, but it only works with one,
    depending on the user's choice. The function finds the minimum and
    maximum elements of the selected list and in the cycle iterates the numbers
    that are not members of the given list in the range from the minimum to
    the maximum element. The function returns new set.
    >>> not_set([5, 2, 8, 12, 3, 7, 10, 23], [6, 23, 56, 3, 1, 3, 9, 0], 1)
    {4, 6, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}
    >>> not_set([5, 2, 8, 12, 3, 7, 10, 23], [6, 23, 3, 1, 3, 9, 0], 2)
    {2, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}
    '''
    n_set = set()

    if numb == 1:
        maxi = max(set1)
        mini = min(set1)
        for i in range(mini, maxi):
            if i not in set1:
                n_set.add(i)
    elif numb == 2:
        orient = max(set2)
        for i in range(orient):
            if i not in set2:
                n_set.add(i)
    else:
        return 'You made a mistake. Try again!'

    return n_set


def common_set(set1, set2):
    '''
    (list, list) -> (set)
    This function takes two lists of numbers and returns a set where all
    the common elements of both lists are present
    >>> common_set([6, 3, 8, 12, 34, 82, 48, 12, 33], [9, 33, 76, 12, 9])
    {33, 12}
    >>> common_set([5, 2, 8, 12, 3, 7, 10, 23], [6, 23, 56, 3, 1, 3, 9, 0])
    {3, 23}
    '''
    c_set = set()

    for i in set1:
        if i in set2:
            c_set.add(i)

    return c_set


def without_set_1(set1, set2):
    '''
    (list, list) -> (set)
    This function takes two lists of numbers and adds to the new set only
    those elements that are in the first list, and which are not in the
    second list.
    >>> without_set_1([5, 2, 8, 12, 3, 7, 10, 23], [6, 23, 3, 1, 3, 9, 0])
    {2, 5, 7, 8, 10, 12}
    '''
    w_set_1 = set()

    for i in set2:
        if i in set1:
            set1.remove(i)

    return set(set1)


def without_set_2(set1, set2):
    '''
    (list, list) -> (set)
    This function takes two lists of numbers and adds to the new set only
    those elements that are in the second list, and which are not in the
    first list.
    >>> without_set_2([5, 2, 8, 12, 3, 7, 10, 23], [6, 23, 3, 1, 3, 9, 0])
    {0, 1, 3, 6, 9}
    '''
    w_set_2 = set()

    for i in set1:
        if i in set2:
            set2.remove(i)

    return set(set2)


def xor(set1, set2):
    '''
    (list, list) -> (set)
    This function takes two lists and returns a new set of elements of both
    lists that exist only in one of these lists
    >>> xor([6, 3, 2, 6, 7, 12, 43, 90, 44], [12, 4, 8, 2, 5, 7, 77, 4, 45])
    {3, 4, 5, 6, 8, 43, 44, 77, 45, 90}
    '''
    x_set = set()

    for i in (set1):
        if i not in set2:
            x_set.add(i)
    for i in (set2):
        if i not in set1:
            x_set.add(i)

    return x_set


set1 = []
set2 = []
print()
print('Hello! This program will help you perform some bit operations')
print('on sets. To enter numbers in the sets start right now with the numbers')
print('of the first set. When you finish with the first set, just press Enter')
print('and the program will go to the second set. When you are done with the ')
print('second set, just press Enter and choose the option that you would like')
print('to perform with your sets.')

while True:
    try:
        numb = int(input('Input number of the first set:' + '\n'))
        set1.append(numb)
    except ValueError:
        break

while True:
    try:
        numb = int(input('Input number of the second set:' + '\n'))
        set2.append(numb)
    except ValueError:
        break

print ('Please, input the number of your operation:')
print('1. Union of the sets')
print('2. Addition of one of the sets')
print('3. Intersection of the sets')
print('4. The first set without the second set')
print('5. The second set without the first set')
print('6. The symmetric difference of the sets')

try:
    oper = int(input())
except ValueError:
    print('Oops! You made a mistake. Try again!')

if oper == 1:
    print('Union of the sets:', union(set1, set2))
elif oper == 2:
    print('Enter the number of the set to which you want to receive the')
    print('addition: 1 or 2?')
    numb = int(input())
    print('Addition of one of the sets:', not_set(set1, set2, numb))
elif oper == 3:
    print('Intersection of the sets:', common_set(set1, set2))
elif oper == 4:
    print('The first set without the second set:', without_set_1(set1, set2))
elif oper == 5:
    print('The second set without the first set:', without_set_2(set1, set2))
elif oper == 6:
    print('The symmetric difference of the sets is:', xor(set1, set2))
else:
    print('Oops! You made a mistake. Try again!')
