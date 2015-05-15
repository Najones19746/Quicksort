__author__ = 'Nick Jones'


def quick(x):
    less = []
    pivotList = []
    more = []
    if len(x) <= 1:
        return x
    else:
        pivot = x[0]
        for number in x:
            number = int(number)
            if number < pivot:
                less.append(number)
            elif number > pivot:
                more.append(number)
            else:
                pivotList.append(number)
        less = quick(less)
        more = quick(more)
        return less + pivotList + more
numbers = raw_input().split(' ')
print quick(numbers)