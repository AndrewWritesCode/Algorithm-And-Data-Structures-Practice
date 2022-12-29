import random


# Arrays A and B of length n will represent binary integers of n bits. Output Array C wil be n + 1 bits

def main(n_bits=8):
    carry_bit = 0
    A, B = [], []
    for i in range(n_bits):  # generate 2 n bit numbers
        A.append(random.randint(0, 1))
        B.append(random.randint(0, 1))
    C = binary_addition(A, B)

    print(f'{A} plus {B} equals {C}')
    print('')
    print(f'{A} in decimal is {binary_to_decimal(A)}')
    print(f'{B} in decimal is {binary_to_decimal(B)}')
    print(f'{binary_to_decimal(A)} + {binary_to_decimal(B)} = {binary_to_decimal(C)},'
          f' {(binary_to_decimal(A) + binary_to_decimal(B)) == binary_to_decimal(C)}')


def binary_addition(array_A, array_B):
    # A + B = C
    array_C = [0] * (max(len(array_A), len(array_B)) + 1)  # add an extra bit to C to prevent bit overflow
    idx = 1
    for i in array_A:
        array_C[-1*idx] += array_A[-1*idx] + array_B[-1*idx]
        if array_C[-1*idx] > 1:  # handles the addition carry operation
            array_C[-1*idx] = array_C[-1*idx] % 2
            array_C[-1*idx - 1] += 1
        idx += 1
    return array_C


def binary_to_decimal(binary_array):
    decimal = 0
    magnitude = 0
    for i in reversed(binary_array):
        decimal += i * (2 ** magnitude)
        magnitude += 1
    return decimal


if __name__ == '__main__':
    main()
