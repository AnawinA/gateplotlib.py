import numpy as np

is_print = False

def possible_bin(bit: int) -> list:
    possible_bin = []
    for i in range(2**bit):
        binary = str(bin(i))[2:].zfill(bit)
        list_bin = [int(x) for x in binary]
        possible_bin.append(list_bin)
    return possible_bin

def k_map(table_result: list[int]) -> None:
    table_result_np = np.array(table_result).reshape(2, 4, order='F')
    table_result_np[:, [3, 2]] = table_result_np[:, [2, 3]]
    return table_result_np

def k_map2(table_result: list[int]) -> None:
    table_result_np = np.array(table_result).reshape(4, 4, order='F')
    table_result_np[:, [3, 2]] = table_result_np[:, [2, 3]]
    table_result_np[[3, 2]] = table_result_np[[2, 3]]
    return table_result_np