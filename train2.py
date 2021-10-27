import math
from numbers import Number
from typing import List, Tuple
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def get_data_from_file():
    with open("File.txt") as file:
        return [line.split() for line in file]


def get_column(matrix, row_number):
    return [float(row[row_number]) for row in matrix]


def get_border_indexes(array: List[float], start_value: float, end_value: float) -> Tuple[int, int]:
    start_index = 0
    end_index = 0
    for index, value in enumerate(array):
        if start_value > value:
            start_index = index
    for index, value in enumerate(array):
        if end_value < value:
            end_index = index
            break
    return start_index, end_index


def calc_T_i(p_a: float, l: float, s_i: float, frequency: float, frequency_i: float, y_i: float, N: float):
    alpha_i = calc_alpha(s_i, frequency, frequency_i, y_i, N)
    return math.exp(-1 * alpha_i * p_a * l)


def calc_alpha(s_i: float, frequency: float, frequency_i: float, y_i: float, N: float):
    left_side = s_i * N / np.pi
    right_side = y_i / ((frequency - frequency_i) ** 2 + y_i ** 2)
    return left_side * right_side


def main():
    data = get_data_from_file()
    iso = get_column(data, 2)
    s = get_column(data, 3)
    g = get_column(data, 4)

    start_index, end_index = get_border_indexes(iso, 6046, 6048)
    new_frequency_range = np.arange(iso[start_index], iso[end_index], 0.01)

    p_a = 1
    l = 7
    frequency = 6046.9647
    S_i = 1.320e-21
    N = 2.479e19
    y_i = 0.0660

    t_i = []
    for frequency_i in new_frequency_range:
        t_i.append(calc_T_i(p_a, l, S_i, frequency, frequency_i, y_i, N))

    sns.lineplot(x=new_frequency_range, y=t_i)
    plt.show()


if __name__ == "__main__":
    main()