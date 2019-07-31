# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2019/7/29 下午10:17
# @File   : selection_sort.py

from functools import wraps
import time

def time_cost(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(f'time cost:{time.time()-start}')
    return wrap

@time_cost
def selection_sort1(arr, length=0):
    '''选择排序算法，O(n^2)'''

    for i in range(length-1):
        min_index = i
        for j in range(i+1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]

    # for i_index, i in enumerate(arr):
    #     min_index = i_index
    #     for j_index, j in enumerate(arr[i_index:], i_index):
    #         if j < arr[min_index]:
    #             min_index = j_index
    #     arr[i_index], arr[min_index] = arr[min_index], arr[i_index]


if __name__ == '__main__':

    import random
    arr1 = [random.randint(0, 1000) for i in range(1000)]
    selection_sort1(arr1, len(arr1))







