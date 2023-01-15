import random


def main(array_length=8):
    array = []
    for i in range(array_length):
        array.append(random.randint(0, 100))

    print(array)
    merge_sort(array)
    print(array)


def merge_sort(array):
    q = int(len(array) / 2)  # midpoint index of array
    if len(array) < 2:  # base case for recursion
        return

    left = array[:q]  # left side of array
    right = array[q:]  # right side of array
    merge_sort(left)
    merge_sort(right)

    i = 0  # left array index
    j = 0  # right array index
    k = 0  # out array index

    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    main()
