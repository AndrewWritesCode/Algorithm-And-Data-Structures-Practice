import random


def main():
    test_array = []
    for i in range(100):
        test_array.append(random.randint(0, 100))
    sorted_array = insertion_sort(test_array.copy())
    r_sorted_array = reverse_insertion_sort(test_array.copy())

    print(f'Original List:         {test_array}')
    print(f'Sorted List:           {sorted_array}')
    print(f'Reverse Sorted List:   {r_sorted_array}')
    # Checksums
    print(f'Original List Checksum:         {sum(test_array)}')
    print(f'Sorted List Checksum:           {sum(sorted_array)}')
    print(f'Reverse Sorted List Checksum:   {sum(r_sorted_array)}')


def insertion_sort(array):
    if len(array) > 1:
        for i in range(len(array) - 1):
            key = array[i + 1]  # index of the current key (so i is the prior key)
            while i >= 0 and array[i] > key:  # get the index of prior keys until prior key is smaller
                array[i + 1] = array[i]
                i -= 1
            array[i + 1] = key  # keep key in position if larger than all prior keys
        return array
    else:
        print(f'Warning: array is too short to sort!')
        return array


def reverse_insertion_sort(array):
    if len(array) > 1:
        for i in range(len(array) - 1):
            key = array[i + 1]  # index of the current key (so i is the prior key)
            while i >= 0 and array[i] < key:  # get the index of prior keys until prior key is larger
                array[i + 1] = array[i]
                i -= 1
            array[i + 1] = key  # keep key in position if smaller than all prior keys
        return array
    else:
        print(f'Warning: array is too short to sort!')
        return array


if __name__ == '__main__':
    main()
