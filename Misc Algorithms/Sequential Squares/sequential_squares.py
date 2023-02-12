import time

# This code will test the speed of calculating sequential squares using various different methods


def get_run_time(fxn, *args):
    def wrapper(*args):
        start_time = time.time()
        ck_sum = sum(fxn(*args))
        finish_t = time.time() - start_time
        print(f'{fxn.__name__}:\n'
              f'Checksum = {ck_sum}\n'
              f'Completed in {finish_t}s\n'
              f'{"#"*60}')
        return ck_sum, finish_t, fxn.__name__
    return wrapper


@get_run_time
def vanilla_s_squares(iter_num):
    num_list = []
    for i in range(iter_num):
        num_list.append(i**2)
    return num_list


# n+1 expansion
# f(x) = x^2, x
# f(x+1) = (x+1)^2 = x^2 + 2x + 1
# 1 = 0 + 2(0) + 1
# 4 = 1 + 2(1) + 1
# 9 = 4 + 2(2) + 1
# 16 = 9 + 2(3) + 1
# 25 = 16 + 2(4) + 1
# N^2 = n^2 + 2(n) + 1

@get_run_time
def np1_s_squares(iter_num):
    num_list = []
    prev_sq = 0  # store previous square instead of recalculating each iteration
    mul_slider = 0  # instead of multiplying 2n each loop, just add 2 from previous iteration
    num_list.append(prev_sq)
    for i in range(iter_num)[1:]:
        sq = prev_sq + mul_slider + 1
        prev_sq = sq
        mul_slider += 2
        num_list.append(sq)
    return num_list


@get_run_time
def square_expansion(iter_num):
    num_list = []
    prev_sq = 0
    num_list.append(prev_sq)
    for i in range(iter_num)[1:]:
        sq = prev_sq + 2*i - 1
        prev_sq = sq
        num_list.append(sq)
    return num_list


def results(stats_l):
    ck_sum_l, finish_t_l, name_l = zip(*stats_l)
    cur_sum = ck_sum_l[0]
    best_t = finish_t_l[0]
    best_n = name_l[0]
    for i in range(len(stats_l)-1):
        if ck_sum_l[i+1] != cur_sum:
            print('Check Sum Error!')
            return
        if best_t > finish_t_l[i+1]:
            best_t = finish_t_l[i+1]
            best_n = name_l[i+1]
    print(f'FINAL RESULTS:\n'
          f'Checksum Result: PASS\n'
          f'Fastest Function: {best_n}\n'
          f'Time: {best_t}s')
    return

def main():
    iter_num = 1000001
    stats = []
    print(f'Calculating squares 0 through {iter_num-1}\n'
          f'{"#"*60}')
    stats.append(vanilla_s_squares(iter_num))
    stats.append(np1_s_squares(iter_num))
    stats.append(square_expansion(iter_num))
    results(stats)

if __name__ == '__main__':
    main()