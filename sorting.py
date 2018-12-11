import random


class X(int):
        def __new__(cls, value, index):
            obj = int.__new__(cls, value)
            obj.index = index
            return obj


def read_array_from_file(filename='data.in'):
    array = []
    line = 1
    with open(filename, 'r') as f:
        for i in f.readlines():
            array.append(X(i, line))
            line += 1
    return array


def write_array_to_file(array, filename='data.out'):
    with open(filename, 'w') as f:
        for x in array:
            f.write('{:22} {:>}\n'.format(str(x), str(x.index)))


def insertion_sort(array):
    for i, key in enumerate(array):
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


def merge_sort(array):
    def merge(left, right):
        merged = []
        i_l, i_r = 0, 0
        while i_l < len(left) and i_r < len(right):
            if left[i_l] <= right[i_r]:
                merged.append(left[i_l])
                i_l += 1
            else:
                merged.append(right[i_r])
                i_r += 1
        return merged + left[i_l:] + right[i_r:]

    if len(array) > 1:
        m = len(array) // 2
        l = merge_sort(array[:m])
        r = merge_sort(array[m:])
        return merge(l, r)
    return array


ar = read_array_from_file()
ar = merge_sort(ar)
write_array_to_file(ar, filename='data.out')


#
# a = list(range(0, 100))
# print(a)
# random.shuffle(a)
# # print(a)
# print(insertion_sort(a))
#
# a = list(range(99, -1, -1))
# print(a)
# print(insertion_sort(a))

# a = list(range(1, 100, 1))
# print(a)
# random.shuffle(a)
# print(a)
# print(merge_sort(a))

# a = list(range(100, 0, -1))
# print(a)
# print(merge_sort(a))

# print(merge_sort(list(range(3, 0,-1))))
# print(read_array_from_file())